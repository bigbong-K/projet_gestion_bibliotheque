from sqlalchemy import Column, Integer, String, Float
from database import Base


class Livre_tab(Base):
    __tablename__ = "livre"
    
    id_livre = Column(Integer, primary_key=True, index=True)
    id_categorie = Column(Integer, nullable=False)
    nom = Column(String, nullable=False)
    prix = Column(Float)
    disponibilite = Column(Integer)
    note = Column(Integer)
    code_upc = Column(String)
    description = Column(String)
    image_url = Column(String)
    lien = Column(String)
    