"""Gerador de eventos financeiros sintéticos."""

from datetime import datetime, timedelta, timezone
from decimal import Decimal
from random import Random
from uuid import NAMESPACE_URL, uuid5


def generate_events(count: int = 5, seed: int = 42) -> list[dict]:
    """Gera eventos reproduzíveis para testes e desenvolvimento."""

    if count < 0:
        raise ValueError("count não pode ser negativo")

    # Random local evita interferir em outros geradores.
    rng = Random(seed)

    # Data fixa garante resultados reproduzíveis.
    base_time = datetime(2026, 1, 1, tzinfo=timezone.utc)

    events = []

    for index in range(count):
        # Valores monetários utilizam Decimal.
        amount = Decimal(rng.randint(100, 100000)) / 100

        # Cada transação recebe uma data UTC.
        event_time = base_time + timedelta(seconds=index)

        # UUID determinístico facilita testes de duplicidade.
        event_id = str(
            uuid5(NAMESPACE_URL, f"financial-event:{seed}:{index}")
        )

        events.append({
            "event_id": event_id,
            "account_id": f"ACC-{rng.randint(1, 100):04d}",
            "amount": str(amount.quantize(Decimal("0.01"))),
            "currency": "BRL",
            "event_time": event_time.isoformat(),
            "status": rng.choice(["APPROVED", "DECLINED"]),
        })

    return events
