# I2 — End-to-End Flow Trace (45 min)

**Goal:** Trace `POST /api/v1/loans` from HTTP entry to DB side effect.

## Required output

1. Entry point (route + file)
2. Step-by-step file and function path
3. External dependencies
4. DB side effects
5. Sequence diagram (Mermaid)
6. Known uncertainty

## Suggested trace path

`app/main.py` → `LoanService.create_loan()` → SQLAlchemy session → `loans` table insert
