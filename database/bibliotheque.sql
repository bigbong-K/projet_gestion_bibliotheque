-- On crée la base de données
CREATE DATABASE bibliotheque;

-- On se connecte à la base de données
\c bibliotheque

-- On crée la table categorie
CREATE TABLE IF NOT EXISTS categorie(
    id_categorie SERIAL PRIMARY KEY,
    nom VARCHAR(50),
    lien VARCHAR(100)
);

-- On crée la table livre
CREATE TABLE IF NOT EXISTS livre(
    id_livre SERIAL PRIMARY KEY,
    id_categorie INT NOT NULL,
    nom VARCHAR(50) NOT NULL,
    prix NUMERIC(6,2),
    disponibilite INT,
    note INT,
    code_upc VARCHAR(50),
    description VARCHAR(300),
    image_url VARCHAR(100),
    lien VARCHAR(100),

    FOREIGN KEY (id_categorie)
    REFERENCES categorie (id_categorie)
    ON DELETE RESTRICT
    ON UPDATE CASCADE
);