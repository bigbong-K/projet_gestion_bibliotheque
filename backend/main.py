from fastapi import FastAPI

import categorie.crud
import livre.crud

from database import Base, engine
# from categorie import models

Base.metadata.create_all(bind=engine)


app = FastAPI(title="API : Gestion de Bibliothèque")

app.include_router(categorie.crud.categrie_router)
app.include_router(livre.crud.livre_router)