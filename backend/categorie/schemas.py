from pydantic import BaseModel


class Categorie(BaseModel):
    nom: str
    lien: str


class CategorieId(Categorie):
    id_categorie: int
    
    class Config:
        orm_mode = True
    
