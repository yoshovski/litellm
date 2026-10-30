"""Exercise database initialization without Docker or application imports."""

import os
import subprocess
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[2] / "scripts/check_proxy_database.sh"
HARNESS = r"""
set -euo pipefail
docker() {
  case "$1" in
    run) cat >/dev/null; return 0 ;;
    network|rm|logs) return 0 ;;
    inspect) echo true; return 0 ;;
    exec)
      shift 2
      case "$1" in
        pg_isready)
          # Temporary Unix-socket readiness must not allow schema creation.
          if [[ " $* " != *" -h 127.0.0.1 "* ]]; then return 0; fi
          count=$(cat "$PROBE_COUNT")
          echo $((count + 1)) >"$PROBE_COUNT"
          [[ "$MODE" == ready && "$count" -ge 2 ]]
          return
          ;;
        createdb)
          if [[ " $* " != *" -h 127.0.0.1 "* ]]; then exit 43; fi
          if [[ $(cat "$PROBE_COUNT") -lt 3 ]]; then exit 44; fi
          # This fixture stops before Prisma and tests database startup only.
          exit 42
          ;;
      esac
      ;;
  esac
  echo "Unexpected Docker invocation: $*" >&2
  exit 45
}
sleep() { :; }
source "$SMOKE_SCRIPT" local/test:fixture
"""


class DatabaseStartupTests(unittest.TestCase):
    def run_startup(self, mode):
        with tempfile.TemporaryDirectory() as directory:
            count = Path(directory) / "probes"
            count.write_text("0")
            result = subprocess.run(
                ["bash", "-c", HARNESS],
                env={
                    **os.environ,
                    "PROBE_COUNT": str(count),
                    "SMOKE_SCRIPT": str(SCRIPT),
                    "MODE": mode,
                },
                capture_output=True,
                stdin=subprocess.DEVNULL,
                text=True,
                timeout=10,
            )
            return result, int(count.read_text())

    def test_waits_for_final_tcp_server_before_creating_database(self):
        result, probes = self.run_startup("ready")
        self.assertEqual(result.returncode, 42, result.stderr)
        self.assertEqual(probes, 3)

    def test_timeout_stops_before_schema_or_proxy_checks(self):
        result, probes = self.run_startup("timeout")
        self.assertEqual(result.returncode, 1, result.stderr)
        self.assertIn("FAIL PostgreSQL did not become TCP-ready", result.stderr)
        self.assertEqual(probes, 60)


if __name__ == "__main__":
    unittest.main()
