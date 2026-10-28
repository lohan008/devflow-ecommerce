
from app import app

def test_rota_inicial():
    cliente = app.test_client()
    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert resposta.json["status"] == "Aplicação funcionando"

def test_rota_produtos():
    cliente = app.test_client()
    resposta = cliente.get("/produtos")

    assert resposta.status_code == 200
    assert len(resposta.json) == 2
