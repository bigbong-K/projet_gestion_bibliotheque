import pandas as pd
import psycopg2 
from dotenv import load_dotenv
import os

# On charge les variables d'environnement
load = load_dotenv()

DATABASE = os.getenv("DATABASE")
USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")


conn = psycopg2.connect(
    database = DATABASE,
    user = USER,
    password = PASSWORD,
    host = HOST,
    port = PORT
)

cursor = conn.cursor()

def insert_dataframe(df:pd.DataFrame, nom_table:str):
    # On recupère chaque valeur du df
    for row in df.values:
        columns = ", ".join(df.columns) # "col1, col2, col3"
        # Répresentant des valeurs du df
        values_p = ", ".join(["%s"]*len(df.columns)) #"%s, %s, %s"
        # On enregistre la valeur
        query = f"INSERT INTO {(nom_table)} ({columns}) VALUES ({values_p})"
        # On execute la syntaxte
        cursor.execute(query, tuple(row))
    conn.commit()
    print(f"Données insérée dans la table {nom_table}")
    
if __name__ == "__main__":
    
    df_categories = pd.read_csv("../data/categories.csv", sep=",")
    df_livres = pd.read_csv("../data/books.csv", sep=",")
    
    # On envoie nos données dans la base de données
    insert_dataframe(df=df_categories, nom_table="categorie")
    insert_dataframe(df=df_livres, nom_table="livre")
    
    # Ferme la connection
    cursor.close()
    conn.close()