from fastapi import FastAPI, HTTPException

from app.models import ConvertRequest, ConvertResponse

# Hardcoded rates relative to USD
RATES_TO_USD = {
    "USD": 1.0,
    "EUR": 0.92,
    "GBP": 0.79,
    "INR": 83.0,
}

app = FastAPI(title="Currency Convert Service", version="1.0.0")


def convert(amount: float, from_currency: str, to_currency: str) -> ConvertResponse:
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in RATES_TO_USD or to_currency not in RATES_TO_USD:
        raise HTTPException(status_code=400, detail="Unsupported currency")

    usd_amount = amount / RATES_TO_USD[from_currency]
    converted = usd_amount * RATES_TO_USD[to_currency]
    rate = RATES_TO_USD[to_currency] / RATES_TO_USD[from_currency]

    return ConvertResponse(
        amount=amount,
        from_currency=from_currency,
        to_currency=to_currency,
        rate=round(rate, 6),
        converted_amount=round(converted, 2),
    )


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/convert", response_model=ConvertResponse)
def convert_endpoint(payload: ConvertRequest) -> ConvertResponse:
    return convert(payload.amount, payload.from_currency, payload.to_currency)
