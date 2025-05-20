from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from sqlalchemy import func, text
from livre.models import Livre_tab
from livre.schemas import Livre_categorie, Livre, LivreId
from categorie.crud import delete_categorie, update_categorie
from categorie.models import Categorie_tab

livre_router = APIRouter()

# ===============LIVRE_GET===================================================

def get_livre_by_id(id:int, db: Session = Depends(get_db)):
    return db.query(Livre_tab).filter(Livre_tab.id_livre == id).first()
    

@livre_router.get("/livre/{id}", tags=["Livre"])
def read_livre(id: int, db: Session = Depends(get_db)) -> LivreId:
    livre = get_livre_by_id(id, db)
    if livre is None:
        raise HTTPException(404, "Livre not found")
    return livre

@livre_router.get("/livres", tags=["Livre"])
def read_livres(skip:int=0, limit:int=5, db: Session = Depends(get_db)) -> LivreId:
    return db.query(Livre_tab).offset(skip).limit(limit).all()

# ===============LIVRE_POST===================================================

@livre_router.post("/livre", tags=["Livre"])
def create_livre(livre_input: Livre, db: Session = Depends(get_db)) -> LivreId:
    # id = db.query(func.max(Livre_tab.id_livre)).scalar() + 1
    # livre = Livre_tab(id_categorie=livre_input.id_categorie, nom=livre_input.nom, prix=livre_input.prix,
    #                   disponibilite=livre_input.disponibilite, note=livre_input.note, code_upc=livre_input.code_upc,
    #                   description=livre_input.description, image_url=livre_input.image_url, lien=livre_input.lien)
    
    livre = Livre_tab(**livre_input.model_dump())
    
    db.add(livre)
    db.commit()
    db.refresh(livre)
    
    return livre

# ===============LIVRE_PUT===================================================

@livre_router.put("/livre/{id}", tags=["Livre"])
def update_livre(id:int, livre_update:Livre, db: Session = Depends(get_db)) -> LivreId:
    livre = get_livre_by_id(id, db)
    if livre is None:
        raise HTTPException(404, "Livre not found")
    
    livre.id_categorie=livre_update.id_categorie
    livre.nom=livre_update.nom
    livre.prix=livre_update.prix
    livre.disponibilite=livre_update.disponibilite
    livre.note=livre_update.note
    livre.code_upc=livre_update.code_upc
    livre.description=livre_update.description
    livre.image_url=livre_update.image_url
    livre.lien=livre_update.lien
    
    db.commit()
    
    return livre

# ===============LIVRE_DELETE===================================================

@livre_router.delete("/livre/{id}", tags=["Livre"])
def delete_livre(id:int, db: Session = Depends(get_db)) -> LivreId:
    livre = get_livre_by_id(id, db)
    if livre is None:
        raise HTTPException(404, "Livre not found")
    
    db.delete(livre)
    db.commit()
    
    return livre
    

@livre_router.get("/categories/livre/{categorie_input}", tags=["Categorie_Livre"])
def read_livre_by_categorie(categorie_input:str="Mystery", db: Session = Depends(get_db)) -> list[Livre_categorie]:
    livre = db.query(Livre_tab).join(Livre_tab.categorie).filter(Categorie_tab.nom.ilike(f"%{categorie_input}%")).limit(5).all()
    if not livre:
        raise HTTPException(404, f"{categorie_input} not among categories")
    return livre


@livre_router.get("/categorie/livre/{nom_input}", tags=["Categorie_Livre"])
def read_livre_by_name(nom_input:str="Le monde magique de Lili", db: Session = Depends(get_db)) -> Livre_categorie:
    livre = db.query(Livre_tab).join(Livre_tab.categorie).filter(Livre_tab.nom.ilike(f"%{nom_input}%")).first()
    if not livre:
        raise HTTPException(404, f"{nom_input} is not among books")
    return livre