# I4 — Polyglot Convert System

FastAPI `/convert` service + Node.js CLI client.

## Two-terminal run

**Terminal 1 — service**

```bash
cd service
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --port 8001
```

**Terminal 2 — client**

```bash
cd client
node cli.js 100 USD EUR
# 100 USD = 92 EUR (rate: 0.92)
```

## Tests

```bash
# Service
cd service && pytest -v

# Client unit test
cd client && npm test
```

## Supported currencies

USD, EUR, GBP, INR (hardcoded rates in `service/app/main.py`).
