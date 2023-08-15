from typing import Union

from fastapi import FastAPI

app = FastAPI()

# @app.get("/")
# def read_root():
    # return {"Hello": "World"}

# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
    # return {"item_id": item_id, "q": q}

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

@app.get("/transactions/last6/{client_id}")
def read_transactions(client_id : int):
    return [
        {"recipient" : "Uber Taxi", "date" : "02-13-2012", "amount" : 948.55},
        {"recipient" : "AT&T", "date" : "02-14-2012", "amount" : 19.99},
        {"recipient" : "Ebay", "date" : "02-18-2012", "amount" : 98.55},
        {"recipient" : "Ebay", "date" : "02-19-2012", "amount" : 45.50},
        {"recipient" : "Air BnB", "date" : "02-22-2012", "amount" : -120.00},
        {"recipient" : "Direct Energy", "date" : "02-23-2012", "amount" : -60.00}
    ]


@app.get("/debits/last2/{client_id}")
def read_transactions(client_id : int):
    return [
        {"recipient" : "Uber Taxi", "frequency" : "monthly", "amount" : 120},
        {"recipient" : "Direct Energy", "frequency" : "monthly", "amount" : 128.99},
    ]
