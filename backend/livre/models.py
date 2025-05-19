import categorie.crud
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
# import categorie.models


class Livre_tab(Base):
    __tablename__ = "livre"
    
    id_livre = Column(Integer, primary_key=True, index=True)
    id_categorie = Column(Integer, ForeignKey("categorie.id_categorie"))
    nom = Column(String, nullable=False)
    prix = Column(Float)
    disponibilite = Column(Integer)
    note = Column(Integer)
    code_upc = Column(String)
    description = Column(String)
    image_url = Column(String)
    lien = Column(String)
    
    categorie = relationship("Categorie_tab", back_populates="livre")
    
    
    
    
    