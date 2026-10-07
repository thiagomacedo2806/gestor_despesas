from django.db import models
from django.http import JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
import json

class Despesa(models.Model):
    """
    Modelo simplificado que representa uma despesa financeira.
    """
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50, blank=True, default="Geral")
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = "despesas"

    def __str__(self) -> str:
        return f"{self.descricao} - R$ {self.valor}"

def listar_despesas(request: HttpRequest) -> JsonResponse:
    """
    Retorna todas as despesas cadastradas no banco de dados.
    """
    despesas = list(Despesa.objects.values("id", "descricao", "valor", "categoria"))
    for d in despesas:
        d["valor"] = float(d["valor"])
    return JsonResponse(despesas, safe=False, json_dumps_params={"ensure_ascii": False})

@csrf_exempt
def criar_despesa(request: HttpRequest) -> JsonResponse:
    """
    Cria uma nova despesa através de uma requisição POST com dados JSON.
    """
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            if not data.get("descricao"):
                return JsonResponse({"erro": "A descrição é obrigatória"}, status=400)
            
            try:
                valor = float(data.get("valor", 0))
                if valor <= 0:
                    return JsonResponse({"erro": "O valor deve ser maior que zero"}, status=400)
            except (ValueError, TypeError):
                return JsonResponse({"erro": "Valor inválido"}, status=400)

            despesa = Despesa.objects.create(
                descricao=data.get("descricao"),
                valor=valor,
                categoria=data.get("categoria", "Geral")
            )
            return JsonResponse({"id": despesa.id, "status": "criado"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"erro": "JSON inválido"}, status=400)
        except Exception as e:
            return JsonResponse({"erro": str(e)}, status=500)
            
    return JsonResponse({"erro": "Método não permitido"}, status=405)