from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
# import livre.models 



class Categorie_tab(Base):
    __tablename__ = "categorie"
    
    id_categorie = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    lien = Column(String)
    
    livre = relationship("Livre_tab", back_populates="categorie")
    