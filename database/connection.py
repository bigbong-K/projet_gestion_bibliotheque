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