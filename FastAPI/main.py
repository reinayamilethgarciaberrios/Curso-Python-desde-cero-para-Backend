
#Documentacion oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI

app = FastAPI()

#Url local: http://127.0.0.1:8000/

@app.get("/")
async def root():
    return{"message": "Hello fastAPI"}

#Inicia el server: uvicorn main:app --reload
#Deter el server: CTRL+C

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}