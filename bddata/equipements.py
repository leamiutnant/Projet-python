import sqlite3

class Equipement:
    """
    classe Equipement avec les attributs, par rapport à ceux qu'on a choisit dans le csv_parser.
    """
    def __init__(self, j, numInstal, nomEq, city):
        """
        Méthode qui initialise l'objet Equipement avec ses attributs
        """
        self.j = j
        self.numInstal = numInstal
        self.nomEq = nomEq
        self.city = city


    def insert(self, c):
        """
        Méthode qui insère les données dans la table correspondante
        """
        #on insère les données dans la table equipements
        insert_query = "INSERT INTO equipements(j,numInstal, nomEq, city) VALUES (?,?,?,?)"
        c.execute(insert_query, (self.j, self.numInstal, self.nomEq, self.city))
