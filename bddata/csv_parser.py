import csv


from activities import Activity
from equipements import Equipement
from installations import Installation

def activities(c):
    """
    Sélection des colonnes importantes, à partir des fichiers csv, à mettre dans la base de données pour la table "activities".
    """
    #lecture du fichier csv
    cr = csv.reader(open("csv/activites.csv","rt"))
    header = True
    #variable j incrémentée dans la boucle pour servir de Primary Key à la table.
    j = 0
    # boucle qui récupère les données des colonnes intéressantes.
    for row in cr:
        if header:
            header = False
            continue

        if not row[2]:
            continue
        else:
            equipId = row[2]
        if not row[5]:
            continue
        else:
            activity = row[5]
        if not row[9]:
            continue
        else:
            level = row[9]

        city = row[1]
        j = j + 1
        a = Activity(j, int(equipId), activity, city, level)
        a.insert(c)
        print("{}/36031".format(j))


def equipements(c):
    """
    Sélection des colonnes importantes, à partir des fichiers csv, à mettre dans la base de données pour la table "equipements".
    """
    #lecture du fichier csv
    cr = csv.reader(open("csv/equipements.csv","rt"))
    header = True
    #variable j incrémentée dans la boucle pour servir de Primary Key à la table.
    j = 0
    # boucle qui récupère les données des colonnes intéressantes.
    for row in cr:
        if header:
            header = False
            continue

        numInstal = row[2]
        nomEq = row[5]
        city = row[1]
        j = j + 1
        e = Equipement(j, int(numInstal), nomEq, city)
        e.insert(c)
        print("{}/20874")


def installations(c):
    """
    Sélection des colonnes importantes, à partir des fichiers csv, à mettre dans la base de données pour la table "installations".
    """
    #lecture du fichier csv
    cr = csv.reader(open("csv/installations.csv","rt"))
    header = True
    #variable j incrémentée dans la boucle pour servir de Primary Key à la table.
    j = 0
    # boucle qui récupère les données des colonnes intéressantes.
    for row in cr:
        if header:
            header = False
            continue

        num = row[1]
        name = row[0]
        city = row[2]
        access = row[12]
        j = j + 1
        i = Installation(j, int(num), name, city, access)
        i.insert(c)
        print("{}/9229")
