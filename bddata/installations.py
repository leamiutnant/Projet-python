import sqlite3

"""
classe Installation avec les attributs, par rapport à ceux qu'on a choisit dans le csv_parser.
"""
class Installation:
    def __init__(self, j, num, name, city, access):
        self.j = j
        self.num = num
        self.name = name
        self.city = city
        self.access = access


    def insert(self, c):
        #on insère les données dans la table installations
        insert_query = "INSERT INTO installations(j, num, name, city, access) VALUES (?,?,?,?,?)"
        c.execute(insert_query, (self.j, self.num, self.name, self.city, self.access))
