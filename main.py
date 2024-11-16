from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/parouimpar/{numero}")
def parOuImpar(numero: int):
    if numero % 2 == 0:
        return {"resposta" : f"O número {numero} é par"}
    else:
        return {"resposta" : f"O número {numero} é impar"}

from datetime import datetime
@app.get("/hora/{cidade}")
def fusoHorario(cidade: str):
    hora = {
        "brasilia": "UTC-3",
        "tokyo": "UTC+9",
        "londres": "UTC+0"
    }
    agora = datetime.utcnow()
    if cidade in hora:
        utc = int(hora[cidade].split("UTC")[1])
        horaCidade = agora.hour + utc
        return {"cidade": cidade, "hora": f"{horaCidade % 24}h"}
    else:
        return {"erro": "Cidade não encontrada"}


# 3. Dia da semana
@app.get("/diasemana")
def diaSemana():
    dia = datetime.now().strftime("%A")
    dias = {
        "Monday": "segunda-feira",
        "Tuesday": "terça-feira",
        "Wednesday": "quarta-feira",
        "Thursday": "quinta-feira",
        "Friday": "sexta-feira",
        "Saturday": "sábado",
        "Sunday": "domingo"
    }
    return {"hoje é": dias[dia]}

# (4) - Retornar frase
@app.get("/frase")
def retornaFrase():
    response = requests.get("https://zenquotes.io/api/today")
    if response.status_code == 200:
        data = response.json()[0]
        frase = data.get("q")
        autor = data.get("a")
        return {"frase": frase, "autor": autor}
    else:
        return {"erro": "Não foi possível obter a frase"}