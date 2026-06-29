FROM ghcr.io/astral-sh/uv:python3.11-bookworm-slim

WORKDIR /app

COPY pyproject.toml .
COPY gsc/ gsc/

RUN uv pip install --system -e .

ENV MCP_TRANSPORT=sse
ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=3001

EXPOSE 3001

CMD ["mcp-search-console"]
