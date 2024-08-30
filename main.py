from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
app = FastAPI()

class Personagem(BaseModel):
    id: int
    Nome: str
    Raridade: str
    Arma: str
    Visão: str



personagens = [
    {"id": 0,"nome": "Ganyu", "Raridade": "5_stars", "Arma": "Arco", "Visão": "Cryo"},
    {"id": 1,"nome": "Hu Tao", "Raridade": "5_stars", "Arma": "Lança", "Visão": "Pyro"},
    {"id": 2,"nome": "Yelan", "Raridade": "5_stars", "Arma": "Arco", "Visão": "Hydro"},
    {"id": 3,"nome": "Furina", "Raridade": "5_stars", "Arma": "Espada", "Visão": "Hydro"},
    {"id": 4,"nome": "Navia", "Raridade": "5_stars", "Arma": "Espadão", "Visão": "Geo"},
    {"id": 5,"nome": "venti", "Raridade": "5_stars", "Arma": "Arco", "Visão": "Anemo"},
    {"id": 6,"nome": "Raiden Shogun", "Raridade": "5_stars", "Arma": "Lança", "Visão": "Electro"},
    {"id": 7,"nome": "Kokomi", "Raridade": "5_stars", "Arma": "Catalizador", "Visão": "Hydro"},
    {"id": 8,"nome": "Eula", "Raridade": "5_stars", "Arma": "Espadão", "Visão": "Cryo"},
    {"id": 9,"nome": "Jean", "Raridade": "5_stars", "Arma": "Espada", "Visão": "Anemo"},
    {"id": 10,"nome": "Bennet", "Raridade": "4_stars", "Arma": "Espada", "Visão": "Pyro"},
    {"id": 11,"nome": "Clorinde", "Raridade": "5_stars", "Arma": "Espada", "Visão": "Electro"},
    
]


@app.get("/")
async def home():
    return personagens

@app.get("/personagem/{id}")
async def pegar_Personagem(id: int):
    return personagens[id]

@app.put("/personagem/{id}", response_model=Personagem)
async def update_Personagem(id: int, personagem: Personagem):
    update_personagem_encoded = jsonable_encoder(personagem)
    personagens[id] = update_personagem_encoded
    return update_personagem_encoded 
