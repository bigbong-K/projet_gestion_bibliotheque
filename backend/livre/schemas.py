from pydantic import BaseModel

class LivreId(BaseModel):
    id_livre: int
    id_categorie: int
    nom: str
    prix: float
    disponibilite: int
    note: int
    code_upc: str
    description: str
    image_url: str
    lien: str
    
    class Config:
        orm_mode = True


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