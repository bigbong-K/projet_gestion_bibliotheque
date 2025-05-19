from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from categorie.schemas import Categorie, CategorieId
from database import engine, get_db
from categorie.models import Categorie_tab
from sqlalchemy import func, text


categrie_router = APIRouter()
# api = FastAPI()

# @categrie_router.get("/")
# def get_index():
#     return {"message" : "Bienvenue sur mon application de gestion de bibliothèque"}

# ========================REQUETTE_GET===============================

def get_categorie_by_id(id: int, db: Session = Depends(get_db)) -> CategorieId:
    return db.query(Categorie_tab).filter(
        Categorie_tab.id_categorie == id
    ).first()
    
    
@categrie_router.get("/categorie/{id}", tags=["Categorie"])
def read_categorie(id:int, db: Session = Depends(get_db)) -> CategorieId:
    categ = get_categorie_by_id(id, db)
    if categ is None:
        raise HTTPException(404, "Categorie not found")
    return categ


@categrie_router.get("/categories", tags=["Categorie"])
def read_categories(skip:int=0, limit:int=5, db: Session = Depends(get_db)) -> list[CategorieId]:
    return db.query(Categorie_tab).offset(skip).limit(limit).all()


# ========================REQUETTE_POST===============================

@categrie_router.post("/categorie", tags=["Categorie"])
def create_categorie(cat_input: Categorie, db: Session = Depends(get_db)) -> CategorieId:
    # new_id = db.query(func.max(Categorie_tab.id_categorie)).scalar() + 1
    categ = Categorie_tab(nom=cat_input.nom, lien=cat_input.lien)
    
    db.add(categ)
    db.commit()
    db.refresh(categ)
    
    return categ

# ========================REQUETTE_PUT===============================

@categrie_router.put("/categorie/{id}", tags=["Categorie"])
def update_categorie(id:int, new_categ:Categorie, db: Session = Depends(get_db)) -> CategorieId:
    categ = get_categorie_by_id(id, db)
    if categ is None:
        raise HTTPException(404, "categorie not found")
    
    categ.nom = new_categ.nom
    categ.lien = new_categ.lien
    
    db.commit()
        
    return categ

# ========================REQUETTE_DELETE===============================

@categrie_router.delete("/categorie/{id}", tags=["Categorie"])
def delete_categorie(id:int, db: Session = Depends(get_db)) -> CategorieId:
    # categ = db.query(Categorie_tab).filter(Categorie_tab.id_categorie == id).first()
    categ = get_categorie_by_id(id, db)
    if categ is None:
        raise HTTPException(404, "Categorie not found")
    
    db.delete(categ)
    db.commit()
    
    return categ
    