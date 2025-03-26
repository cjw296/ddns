# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

LABEL org.opencontainers.image.title="A quick and dirty image to update DDNS"

# This is the one that's shown on https://github.com/cjw296/ddns/pkgs/container/ddns
LABEL org.opencontainers.image.description="Provides a quick and dirty script to update DDNS"

# Install the project into `/app`
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

COPY . /app
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev

# https://github.com/astral-sh/uv/issues/12202#issuecomment-2755103920
ENTRYPOINT [".venv/bin/python", "client.py"]
