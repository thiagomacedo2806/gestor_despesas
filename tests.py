import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "manage")
django.setup()

from django.test import TestCase, Client
from despesas import Despesa

class DespesasTestCase(TestCase):
    """
    Conjunto de testes automatizados para verificar as operações do Gestor de Despesas.
    """
    def setUp(self) -> None:
        self.client = Client()

    def test_fluxo_gerenciamento_despesas(self) -> None:
        payload = {
            "descricao": "Almoço de negócios",
            "valor": 45.90,
            "categoria": "Alimentação"
        }
        response_criar = self.client.post(
            "/criar/",
            data=json.dumps(payload),
            content_type="application/json"
        )
        self.assertEqual(response_criar.status_code, 201)
        self.assertIn("id", response_criar.json())

        response_listar = self.client.get("/")
        self.assertEqual(response_listar.status_code, 200)
        despesas = response_listar.json()
        self.assertEqual(len(despesas), 1)
        self.assertEqual(despesas[0]["descricao"], "Almoço de negócios")
        self.assertEqual(despesas[0]["valor"], 45.90)

        response_invalido_descricao = self.client.post(
            "/criar/",
            data=json.dumps({"valor": 10.0}),
            content_type="application/json"
        )
        self.assertEqual(response_invalido_descricao.status_code, 400)

        response_invalido_valor = self.client.post(
            "/criar/",
            data=json.dumps({"descricao": "Uber", "valor": -5.0}),
            content_type="application/json"
        )
        self.assertEqual(response_invalido_valor.status_code, 400)