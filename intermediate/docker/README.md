# I5 — Dockerize FastAPI Transaction Service

Containerizes the B4 FastAPI service.

## Build (from repo root)

```bash
docker build -f intermediate/docker/Dockerfile -t transactions-api .
```

## Run

```bash
docker run --rm -p 8000:8000 transactions-api
```

## Health check proof

```bash
curl http://localhost:8000/health
# {"status":"ok"}

curl -X POST http://localhost:8000/transactions \
  -H "Content-Type: application/json" \
  -d '{"amount": 50, "type": "credit", "description": "Docker test"}'

curl http://localhost:8000/balance
```

## Dockerfile features

- Python 3.12 slim base
- Built-in `HEALTHCHECK` against `/health`
- Exposes port 8000
