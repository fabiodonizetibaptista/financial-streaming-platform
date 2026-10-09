# Architecture Design

Status: Draft v0.1

## Business Scenario

A simulated financial platform receives continuous transaction
events and provides reliable operational analytics.

## Target Architecture

```text
Python Event Producer
        |
        v
Apache Kafka (KRaft)
        |
        v
Spark Structured Streaming
        |
        +----> Valid Events ---> Analytical Storage
        |
        +----> Invalid Events -> Quarantine / DLQ
```

## Initial Event Contract

| Field | Description |
|---|---|
| event_id | Deterministic unique event identifier |
| account_id | Synthetic account identifier |
| amount | Decimal-compatible monetary string |
| currency | ISO currency code |
| event_time | UTC event timestamp |
| status | APPROVED or DECLINED |

## Architectural Principles

- Reproducible synthetic data
- Explicit event contracts
- Idempotent processing
- Automated tests
- Fault recovery
- Data quality and reconciliation
- Observability
- No real financial credentials

## Decisions Pending

- Kafka topic configuration and partition keys
- Schema Registry and compatibility strategy
- Watermarks and late-event handling
- Deduplication and delivery guarantees
- Checkpointing and restart behavior
- Storage format and transactional guarantees
- Resource constraints in GitHub Codespaces

## Limitations

The current milestone implements only local event generation.
Kafka, Spark and analytical storage remain future milestones.
Exactly-once end-to-end behavior is not claimed.
