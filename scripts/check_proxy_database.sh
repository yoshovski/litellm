#!/usr/bin/env bash
# Disposable database smoke test: no deployment config, provider credentials or host ports.
set -euo pipefail
image=${1:?Usage: check_proxy_database.sh IMAGE}
run_id="litellm-prisma-${RANDOM}-$$"
network_name="$run_id-net"
database_name="$run_id-db"
proxy_name="$run_id-proxy"
cleanup() {
  docker rm -fv "$proxy_name" "$database_name" >/dev/null 2>&1 || true
  docker network rm "$network_name" >/dev/null 2>&1 || true
}
trap cleanup EXIT

docker run --rm --network none --cap-drop ALL --security-opt no-new-privileges \
  --entrypoint python -i "$image" -B - <<'PY'
import ctypes
import subprocess
ctypes.CDLL('libssl.so.3')
ctypes.CDLL('libcrypto.so.3')
r = subprocess.run(['prisma', 'version'], capture_output=True, text=True, check=True)
assert 'debian-openssl-3.0.x' in r.stdout, r.stdout
assert 'query-engine ' in r.stdout and 'schema-engine-cli ' in r.stdout, r.stdout
print('PASS Prisma query/schema engines load with OpenSSL 3 compatibility libraries')
PY

docker network create --internal "$network_name" >/dev/null
docker run -d --name "$database_name" --network "$network_name" \
  --memory 1g -e POSTGRES_PASSWORD=ci-prisma-only -e POSTGRES_DB=litellm \
  postgres:15-alpine@sha256:b3968e348b48f1198cc6de6611d055dbad91cd561b7990c406c3fc28d7095b21 >/dev/null
database_ready=0
for attempt in $(seq 1 60); do
  # Initialization uses a temporary Unix-socket server; wait for the final TCP server.
  if docker exec "$database_name" pg_isready -h 127.0.0.1 -U postgres -d litellm >/dev/null 2>&1; then
    database_ready=1
    break
  fi
  if [ "$(docker inspect --format '{{.State.Running}}' "$database_name")" != true ]; then break; fi
  sleep 1
done
if [ "$database_ready" != 1 ]; then
  docker logs "$database_name"
  echo 'FAIL PostgreSQL did not become TCP-ready' >&2
  exit 1
fi
docker exec "$database_name" createdb -h 127.0.0.1 -U postgres engine_test
fixture_url="postgresql://postgres:ci-prisma-only@$database_name:5432/engine_test"
docker run --rm --network "$network_name" --cap-drop ALL --security-opt no-new-privileges \
  -e DATABASE_URL="$fixture_url" --entrypoint prisma "$image" db push --schema=/app/schema.prisma --skip-generate

docker run --rm -i --network "$network_name" --cap-drop ALL --security-opt no-new-privileges \
  -e DATABASE_URL="$fixture_url" --entrypoint python "$image" -B - <<'PY'
import asyncio
from prisma import Prisma
async def main():
    db = Prisma()
    await db.connect()
    try:
        assert await db.litellm_proxymodeltable.count() == 0
    finally:
        await db.disconnect()
    print('PASS generated Prisma client connects and reads the fixture database')
asyncio.run(main())
PY

# Start the actual entrypoint against a separate empty database and require migration success.
docker run -d --name "$proxy_name" --network "$network_name" \
  --memory 2g --cap-drop ALL --security-opt no-new-privileges \
  -e DATABASE_URL="postgresql://postgres:ci-prisma-only@$database_name:5432/litellm" \
  -e LITELLM_MASTER_KEY=sk-ci-prisma-runtime-only -e STORE_MODEL_IN_DB=true \
  -e ENFORCE_PRISMA_MIGRATION_CHECK=true "$image" --port 4000 >/dev/null
ready=0
for attempt in $(seq 1 80); do
  if docker exec "$proxy_name" python -B -c 'import os,urllib.request; r=urllib.request.urlopen(urllib.request.Request("http://127.0.0.1:4000/health/readiness",headers={"Authorization":"Bearer "+os.environ["LITELLM_MASTER_KEY"]}),timeout=3); assert r.status==200' >/dev/null 2>&1; then
    ready=1
    break
  fi
  if [ "$(docker inspect --format '{{.State.Running}}' "$proxy_name")" != true ]; then break; fi
  sleep 3
done
if [ "$ready" != 1 ]; then
  docker logs "$proxy_name"
  echo 'FAIL proxy did not become database-ready' >&2
  exit 1
fi
docker exec -i "$proxy_name" python -B - <<'PY'
import os, urllib.request
for path in ['/health/liveliness', '/health/readiness', '/v1/models', '/ui/']:
    request = urllib.request.Request('http://127.0.0.1:4000'+path,
        headers={'Authorization':'Bearer '+os.environ['LITELLM_MASTER_KEY']})
    with urllib.request.urlopen(request, timeout=10) as response:
        assert response.status == 200
    print('PASS proxy HTTP '+path)
PY
