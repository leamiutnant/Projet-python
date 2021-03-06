import sqlite3

"""
classe Activity avec les attributs, par rapport à ceux qu'on a choisit dans le csv_parser.
"""
class Activity:
    """
        Méthode qui initialise l'objet Activity avec ses attributs
    """
    def __init__(self, j, equipId, activity, city, level):
        self.j = j
        self.equipId = equipId
        self.activity = activity
        self.city = city
        self.level = level


    def insert(self, c):
        """
        Méthode qui insère les données dans la table correspondante
        """
        #on insère les données dans la table activities
        insert_query = "INSERT INTO activities(j, equipId, activity, city, level) VALUES (?,?,?,?,?)"
        c.execute(insert_query, (self.j, self.equipId, self.activity, self.city, self.level))
