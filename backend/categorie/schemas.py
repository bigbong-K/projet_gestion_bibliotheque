from pydantic import BaseModel

class CategorieId(BaseModel):
    id_categorie: int
    nom: str
    lien: str
    
    class Config:
        orm_mode = True
    
class Categorie(BaseModel):
    nom: str
    lien: str