# I1 — ER Diagram from Repo (45 min)

**Goal:** Build an ER diagram for all tables/entities using only the repo as source.

## Required output

1. List of tables and entities with primary keys
2. Foreign keys or inferred relationships
3. **Source file path for each claim**
4. Valid Mermaid ER diagram

## Starter Mermaid template

```mermaid
erDiagram
    MEMBERS ||--o{ LOANS : has
    BOOKS ||--o{ LOANS : has
    MEMBERS {
        int id PK
        string email
        string name
    }
```

Cite `app/models.py` for every entity and relationship.
