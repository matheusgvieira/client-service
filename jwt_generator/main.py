from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .jwt_generator import generate_jwt

app = FastAPI()


class Cliente(BaseModel):
    nome_completo: str
    endereco: str
    email: str
    client_id: str
    client_secret: str
    data_inclusao: str


@app.post("/generate_jwt/")
def create_jwt(cliente: Cliente):
    try:
        token = generate_jwt(cliente.dict())
        return {"jwt": token}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
