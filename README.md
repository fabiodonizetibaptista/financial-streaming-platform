# Financial Streaming Platform

Event-driven financial data engineering platform.

## Business Problem

Simulate a financial platform receiving continuous payment events.
The goal is to process transactions reliably, including duplicates,
invalid events, late arrivals and recovery after failures.

## Technology Stack

- Python
- Apache Kafka (planned)
- Apache Spark Structured Streaming (planned)
- Docker (planned)
- GitHub Actions

## Current Status

**Milestone 0 - Project Foundation**

Implemented:
- Deterministic synthetic financial event generator
- JSON serialization
- Automated unit tests
- Initial architecture documentation
- Continuous Integration

Kafka and Spark are not yet implemented.

## Architecture

See [Architecture Design](docs/architecture.md).

## Run Locally

Requires Python 3.11 or newer.

Generate five synthetic events:

```bash
PYTHONPATH=src python3 -m financial_streaming.producer
```

Run tests:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```

## Security

All transactions are synthetic. The project must not contain
real customer data, passwords, financial credentials or tokens.

## Roadmap

1. Foundation and event contracts
2. Kafka producer and consumer
3. Spark Structured Streaming
4. Reliability, recovery and data quality
5. Observability, CI and release
