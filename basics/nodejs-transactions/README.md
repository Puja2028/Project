# B5 — Node.js Transaction Service

Node.js equivalent of the FastAPI transaction service (B4).

## Endpoints

Same contract as B4: `POST /transactions`, `GET /transactions`, `GET /balance`, `GET /health`.

## Install & run

```bash
npm install   # no external deps; validates package
npm start
```

Server runs on port 3000 (override with `PORT`).

## Test

```bash
npm test
```

## Example

```bash
curl -X POST http://localhost:3000/transactions \
  -H "Content-Type: application/json" \
  -d '{"amount": 100, "type": "credit", "description": "Deposit"}'

curl http://localhost:3000/transactions
curl http://localhost:3000/balance
```
