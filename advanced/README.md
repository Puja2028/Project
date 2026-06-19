# Advanced Tasks (A1–A6)

These tasks are **briefs for you to execute** with a coding agent. No starter code is provided — that is intentional.

---

## A1. Multi-worktree parallel plan (45 min)

Take one feature or analysis task and split it safely into parallel worktrees or agent sessions.

**Deliverables:**
- Task decomposition
- Worktree or branch names
- Agent prompt for each lane
- Shared constraints
- Merge order
- Conflict or risk plan
- Verification plan

---

## A2. Execute two parallel worktrees (90 min)

Create two parallel worktrees or branches, make independent changes, then reconcile cleanly.

**Deliverables:**
- Commands used to create worktrees
- Branch or worktree names
- Separate outputs from each lane
- Final merge or reconcile steps
- Test result
- Conflict notes

**Suggested practice:** Split `sample-repo` — lane 1 adds a `GET /api/v1/members` list endpoint; lane 2 adds overdue-loan test coverage.

---

## A3. Polyglot mini-system: FastAPI + Node worker + Rust engine (150 min)

Build a mini fraud-score system:
- **FastAPI** accepts transactions
- **Node.js worker** processes them
- **Rust CLI/library** computes risk score

**Deliverables:**
- FastAPI ingestion endpoint
- Node.js worker process
- Rust scoring CLI or library
- Clear data contract between components
- Tests for core scoring + one integration path
- README with run order

---

## A4. Repository modernization plan + first step (90 min)

Analyze `sample-repo` for modernization opportunities, prioritize, implement highest-value lowest-risk first step.

**Deliverables:**
- Findings with evidence from files/configs
- Prioritized plan
- First step implemented
- Verification (build, tests, lint)
- Rollback notes

---

## A5. Agent code review and adversarial verification (60 min)

Review an agent-generated PR; find correctness, security, test, performance, and maintainability issues.

**Deliverables:**
- Issue list with severity (blocking / non-blocking)
- Suggested fix per issue
- Test or verification steps

---

## A6. Performance profiling and targeted improvement (90 min)

Find a real bottleneck in a small service; make a measurable, minimal improvement.

**Deliverables:**
- Baseline measurement with method and numbers
- Profiling approach and findings
- Bottleneck explanation
- Targeted code change (small, focused)
- After measurement showing improvement
- Tests proving behavior unchanged

**Suggested target:** Profile `sample-repo` loan listing or the Rust log counter on a large file.
