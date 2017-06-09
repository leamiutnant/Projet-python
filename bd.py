import sqlite3
from csv_parser import activities
from csv_parser import equipements
from csv_parser import installations

"""
Ouverture d'une connexion à la base de données et construction des tables dans la base database.bd
"""
# ouvre la connexion à la base de données
conn = sqlite3.connect("database.db")
c = conn.cursor()

# on efface les tables s'il elles étaient existantes, ce qui permet de les modifier
# et on les créer pour leurs ajouter les données choisies.
c.execute("DROP TABLE IF EXISTS equipements")
c.execute("CREATE TABLE equipements (j integer PRIMARY KEY, numInstal integer, nomEq text , city text)")
c.execute("DROP TABLE IF EXISTS installations")
c.execute("CREATE TABLE installations (j integer PRIMARY KEY, num integer, name text, city text, access text)")
c.execute("DROP TABLE IF EXISTS activities")
c.execute("CREATE TABLE activities (j integer PRIMARY KEY, equipId integer, activity text, city text, level text)")

#on fait un commit pour mettre à jour
conn.commit()

activities(c)
equipements(c)
installations(c)

#commit et on ferme la connextion
conn.commit()
conn.close()
