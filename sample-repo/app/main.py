from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from app.config import API_PREFIX
from app.models import SessionLocal, init_db
from app.repositories import BookRepository, LoanService, MemberRepository
from app.schemas import (
    BookCreate,
    BookOut,
    HealthResponse,
    LoanCreate,
    LoanListResponse,
    LoanOut,
    MemberCreate,
    MemberOut,
)

app = FastAPI(title="Library API", version="1.0.0")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
def on_startup():
    init_db()


@app.get(f"{API_PREFIX}/health", response_model=HealthResponse)
def health():
    from datetime import datetime

    return HealthResponse(status="ok", timestamp=datetime.utcnow())


@app.post(f"{API_PREFIX}/members", response_model=MemberOut, status_code=201)
def create_member(payload: MemberCreate, db: Session = Depends(get_db)):
    repo = MemberRepository(db)
    return repo.create(payload.email, payload.name)


@app.get(f"{API_PREFIX}/members/{{member_id}}", response_model=MemberOut)
def get_member(member_id: int, db: Session = Depends(get_db)):
    repo = MemberRepository(db)
    member = repo.get(member_id)
    if not member:
        raise HTTPException(status_code=404, detail="Member not found")
    return member


@app.post(f"{API_PREFIX}/books", response_model=BookOut, status_code=201)
def create_book(payload: BookCreate, db: Session = Depends(get_db)):
    repo = BookRepository(db)
    return repo.create(payload.isbn, payload.title, payload.author)


@app.get(f"{API_PREFIX}/books", response_model=list[BookOut])
def list_books(db: Session = Depends(get_db)):
    repo = BookRepository(db)
    return repo.list_all()


@app.post(f"{API_PREFIX}/loans", response_model=LoanOut, status_code=201)
def create_loan(payload: LoanCreate, db: Session = Depends(get_db)):
    service = LoanService(db)
    try:
        return service.create_loan(payload.member_id, payload.book_id, payload.days)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get(f"{API_PREFIX}/loans/open", response_model=LoanListResponse)
def list_open_loans(db: Session = Depends(get_db)):
    service = LoanService(db)
    return LoanListResponse(loans=service.list_open_loans())
