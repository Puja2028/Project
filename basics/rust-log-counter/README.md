# B6 — Rust Log Counter CLI

Counts `INFO`, `WARN`, and `ERROR` occurrences in a log file.

## Build & test

```bash
cargo test
cargo build --release
```

## Run

```bash
cargo run -- sample.log
```

Expected output:

```
INFO: 3
WARN: 2
ERROR: 2
```

## Missing file

```bash
cargo run -- missing.log
# Error: file not found: missing.log
# exit code 2
```

## Requirements met

- Cargo project
- CLI accepts file path argument
- Counts INFO / WARN / ERROR
- Handles missing file gracefully
- 4 tests (3+ required)
- README with cargo commands
