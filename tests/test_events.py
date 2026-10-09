"""Testes automatizados do gerador de eventos financeiros."""

import unittest
from datetime import datetime
from decimal import Decimal
from uuid import UUID

from financial_streaming.events import generate_events


class TestGenerateEvents(unittest.TestCase):

    def test_quantidade(self):
        """A quantidade gerada deve ser a solicitada."""
        self.assertEqual(len(generate_events(10)), 10)

    def test_determinismo(self):
        """Mesmos parâmetros devem gerar eventos idênticos."""
        self.assertEqual(
            generate_events(10, seed=7),
            generate_events(10, seed=7),
        )

    def test_ids_unicos(self):
        """Cada evento deve possuir um identificador único."""
        events = generate_events(100)
        ids = [event["event_id"] for event in events]
        self.assertEqual(len(ids), len(set(ids)))

        for event_id in ids:
            UUID(event_id)

    def test_contrato(self):
        """Os eventos devem respeitar o contrato inicial."""
        event = generate_events(1)[0]

        campos = {
            "event_id",
            "account_id",
            "amount",
            "currency",
            "event_time",
            "status",
        }

        self.assertEqual(set(event.keys()), campos)
        self.assertEqual(event["currency"], "BRL")
        self.assertIn(event["status"], ("APPROVED", "DECLINED"))
        self.assertGreater(Decimal(event["amount"]), 0)

        timestamp = datetime.fromisoformat(event["event_time"])
        self.assertIsNotNone(timestamp.tzinfo)

    def test_quantidade_negativa(self):
        """Quantidades negativas devem ser rejeitadas."""
        with self.assertRaises(ValueError):
            generate_events(-1)

    def test_lista_vazia(self):
        """Solicitar zero eventos deve retornar uma lista vazia."""
        self.assertEqual(generate_events(0), [])


if __name__ == "__main__":
    unittest.main()
