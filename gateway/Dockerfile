ARG LITELLM_BUILD_IMAGE=cgr.dev/chainguard/wolfi-base@sha256:f15fea2f49cb14dceaea491fcbde0d35e0c190126a744ac05a9838440d47d994
ARG LITELLM_RUNTIME_IMAGE=cgr.dev/chainguard/wolfi-base@sha256:f15fea2f49cb14dceaea491fcbde0d35e0c190126a744ac05a9838440d47d994
ARG UV_IMAGE=ghcr.io/astral-sh/uv:0.13.4@sha256:9f130421e930bfbdc563c00740466603f8723158e90297d07957c2294640262b

FROM $UV_IMAGE AS uvbin

# ---------- Builder ----------
FROM $LITELLM_BUILD_IMAGE AS builder

WORKDIR /app
USER root

COPY --from=uvbin /uv /uvx /usr/local/bin/

RUN apk add --no-cache "ca-certificates-bundle>=20260909-r3" bash gcc python-3.13 python-3.13-dev openssl libssl3 libcrypto3 openssl-dev libsndfile

# UV_COMPILE_BYTECODE=1   precompiles .pyc at install time → faster cold start.
# UV_LINK_MODE=copy       avoids hardlink warnings when uv installs from a
#                         BuildKit cache mount (different filesystem).
# UV_PYTHON_DOWNLOADS=0   force uv to use the apk-installed CPython instead of
#                         silently pulling a managed interpreter.
ENV UV_PROJECT_ENVIRONMENT=/app/.venv \
    UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=0 \
    PATH="/app/.venv/bin:${PATH}"

# Stage 1 — install dependencies only.
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=enterprise/pyproject.toml,target=enterprise/pyproject.toml \
    --mount=type=bind,source=litellm-proxy-extras/pyproject.toml,target=litellm-proxy-extras/pyproject.toml \
    uv sync --frozen --no-install-project --no-install-workspace --no-default-groups --no-editable \
        --extra proxy \
        --extra proxy-runtime \
        --extra extra_proxy \
        --extra semantic-router \
        --python python3

# Stage 2 — copy source and install the project + workspace members.
COPY . .

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-default-groups --no-editable \
        --extra proxy \
        --extra proxy-runtime \
        --extra extra_proxy \
        --extra semantic-router \
        --python python3

RUN mkdir -p /home/nonroot && \
    HOME=/home/nonroot prisma generate --schema=./schema.prisma && \
    chown -R nonroot:nonroot /home/nonroot/.cache

# ---------- Runtime ----------
FROM $LITELLM_RUNTIME_IMAGE AS runtime

USER root

RUN apk add --no-cache "ca-certificates-bundle>=20260909-r3" bash openssl libssl3 libcrypto3 tzdata python-3.13 libsndfile libatomic

# wolfi-base ships an unprivileged `nonroot` account (UID/GID 65532) with
# /home/nonroot. We run the proxy as that user.
WORKDIR /app
ENV HOME=/home/nonroot \
    PATH="/app/.venv/bin:${PATH}" \
    PYTHONPATH="/app" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY --from=builder --chown=nonroot:nonroot /app /app
COPY --from=builder --chown=nonroot:nonroot /home/nonroot/.cache /home/nonroot/.cache

RUN find /app/.venv -type f -path "*/tornado/test/*" -delete && \
    find /app/.venv -type d -path "*/tornado/test" -delete

USER nonroot

EXPOSE 4000/tcp

ENTRYPOINT ["sh", "-c", "exec uvicorn gateway.main:app --workers \"${NUM_WORKERS:-1}\" \"$@\"", "--"]
CMD ["--host", "0.0.0.0", "--port", "4000"]
