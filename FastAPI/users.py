from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

    #users = [User("Brais","moure","https://moure.dev", 35)]

@app.get("/users")
async def users():
    return [{"name": "Brais", "surname": "moure","url":"https://moure.dev"},
            {"name": "Haakon", "surname": "Dahlberg","url":"https://moure.dev"},
            {"name": "Moure", "surname": "Dev","url":"https://moure.dev"}]

