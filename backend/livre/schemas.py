from pydantic import BaseModel
from categorie.schemas import Categorie


class Livre(BaseModel):
    id_categorie: int
    nom: str
    prix: float
    disponibilite: int
    note: int
    code_upc: str
    description: str
    image_url: str
    lien: str


class LivreId(Livre):
    id_livre: int
    
    class Config:
        orm_mode = True
        

class Livre_categorie(BaseModel):
    nom: str
    prix: float
    note: int
    disponibilite: int
    categorie: Categorie
    
    class Config:
        orm_mode = True


