# schemas.py
from pydantic import BaseModel
class ProdutoBase(BaseModel):
    nome: str
    preco: float
    quantidade: int
class ProdutoCreate(ProdutoBase):
    pass
class ProdutoResponse(ProdutoBase):
    id: int
class Config:
    from_attributes = True

#Pet

class PetBase(BaseModel):
    nome: str
    especie: str
    raca: str
    idade: int
class PetCreate(PetBase):
    pass
class PetResponse(PetBase):
    id: int
class Config:
    from_attributes = True