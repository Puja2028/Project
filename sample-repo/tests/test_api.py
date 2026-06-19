import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app, get_db
from app.models import Base, Book, Loan, Member  # noqa: F401 — register models

SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(bind=engine)


@pytest.fixture()
def client(monkeypatch):
    monkeypatch.setattr("app.main.init_db", lambda: None)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    def override_get_db():
        db = TestingSessionLocal()
        try:
            yield db
        finally:
            db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()
    Base.metadata.drop_all(bind=engine)


def test_health(client):
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_member_and_book_flow(client):
    member = client.post(
        "/api/v1/members",
        json={"email": "alice@example.com", "name": "Alice"},
    )
    assert member.status_code == 201
    member_id = member.json()["id"]

    book = client.post(
        "/api/v1/books",
        json={"isbn": "978-0", "title": "Dune", "author": "Herbert"},
    )
    assert book.status_code == 201
    book_id = book.json()["id"]

    loan = client.post(
        "/api/v1/loans",
        json={"member_id": member_id, "book_id": book_id, "days": 7},
    )
    assert loan.status_code == 201
    assert loan.json()["status"] == "open"
