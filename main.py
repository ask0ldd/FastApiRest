from typing import Union

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/client/{client_id}")
def read_client(client_id : int):
    return {
        "name" : "Tony Montana",
        "IBAN" : "NL89RABO1289364745",
        "ClientID" : "X458-89995",
        "Balance" : 3601,
        "Income" : 1601,
        "Expenses" : 901,
    }

@app.get("/cryptos/{client_id}")
def read_cryptos(client_id : int):
    return [
        {"currency" : "bitcoin", "value" : 47223, "amount" : 0.8, "lastmonthvalue" : 44000},
        {"currency" : "ethereum", "value" : 3277, "amount" : 0.3, "lastmonthvalue" : 3000},
        {"currency" : "binance coin", "value" : 240, "amount" : 10, "lastmonthvalue" : 260},
    ]