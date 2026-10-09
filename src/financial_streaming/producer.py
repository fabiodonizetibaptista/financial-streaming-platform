"""Simulador inicial de produção de transações financeiras."""

import json

from financial_streaming.events import generate_events


def main() -> None:
    """Exibe cinco eventos financeiros em formato JSON."""

    for event in generate_events():
        print(json.dumps(event, ensure_ascii=False))


if __name__ == "__main__":
    main()
