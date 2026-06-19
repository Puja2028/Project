# Infra & DevOps Tasks (D1–D6)

Platform artifacts that must **parse and run** with proof. Prefer local or dry-run verification over real cloud spend.

---

## D1. Terraform plan for a small service (60 min)

Write Terraform for a small service (e.g. S3 + Lambda + API Gateway, or GCS + Cloud Run).

**Deliverables:**
- `.tf` files and variables
- Provider and backend configuration
- `terraform validate` output
- `terraform plan` output (local or test backend)
- README with apply/destroy commands

---

## D2. docker-compose stack with end-to-end tests (90 min)

Multi-service stack: API + database + worker, with seed data and one-command E2E test suite.

**Deliverables:**
- `docker-compose.yml` and per-service Dockerfiles
- Seed or fixture script
- One-command test run (all green)
- Logs proving services communicated
- Teardown + clean re-up from zero

**Suggested base:** Extend `sample-repo` with Postgres in compose.

---

## D3. CI pipeline: lint, test, build image (45 min)

GitHub Actions or GitLab CI: on every push, lint, test, build and tag container image.

**Deliverables:**
- Workflow YAML
- Cache/matrix config if relevant
- Link to or local `act` run (passing)
- Failure mode demo (broken commit fails pipeline)

---

## D4. Kubernetes manifests on local cluster (60 min)

Deployment, Service, ConfigMap, optional Ingress for an existing service.

**Deliverables:**
- Manifest YAML files
- Dry-run or kubeval output
- `kubectl apply` on kind/minikube
- curl or port-forward proof
- README with up/down commands

---

## D5. Reproducible dev environment from fresh clone (45 min)

Single-command bootstrap: devcontainer, Nix flake, or Makefile + mise/asdf.

**Deliverables:**
- Bootstrap config files
- Single command and full output
- Passing test run
- Notes on previously implicit deps (packages, env vars, versions)

---

## D6. Observability bolt-on: metrics + dashboard (60 min)

Structured logging + `/metrics` endpoint; Prometheus + Grafana compose with one working dashboard panel.

**Deliverables:**
- Code diff (logs + metrics)
- docker-compose for Prometheus/Grafana with provisioned datasource + dashboard
- Load script generating traffic
- Screenshot or JSON of dashboard panel with live data
- README with run order

**Suggested base:** Add Prometheus metrics to `basics/fastapi-transactions`.
