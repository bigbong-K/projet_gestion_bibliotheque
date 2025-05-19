from sqlalchemy import Column, Integer, String
from database import Base


class Categorie_tab(Base):
    __tablename__ = "categorie"
    
    id_categorie = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    lien = Column(String)
    