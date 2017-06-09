import sqlite3

from libs.bottle import get, post, request, route, template, run

"""
Serveur qui va permettre d'intéragir avec les données de la bd et celles qu'on utilise dans les templates,
en utilisant la librairie bottle.
"""

@route('/home')
def home():
    """
    Lancement de la page où l'on doit sélectionner une city et/ou une activité,
    la page d'acceuil, en lui envoyant les données des villes et des activites.
    """
    conn = sqlite3.connect("../bddata/database.db")
    c = conn.cursor()
    city = c.execute("SELECT a.city from activities a;")
    l_city = [a for a in city]

    cities = []
    for a in l_city:
        cities.append(a[0])
    cities = sorted(set(cities))


    activity = c.execute("SELECT a.activity from activities a;")
    l_activity = [a for a in activity]
    c.close()

    activities = []
    for a in l_activity:
        activities.append(a[0])
    activities = sorted(set(activities))
    return template('tpl/tmpt_search', city = cities, activity = activities)

@post('/search')
def search():
    """
    Méthode qui fait les requêtes sql pour afficher les résultats en fonction de la recherche effectuée.
    Elle récupère ce qui a été sélectionner sur le template tmpt_search.
    """
    try:
        #on se connecte à la bd.
        conn = sqlite3.connect("../bddata/database.db")
        c = conn.cursor()
        #on récupère la ville et l'activité qui ont été sélectionné.
        city = request.forms.get('city')
        activity = request.forms.get('activity')
        #Si l'utilisateur a sélectionné seulement une city on affiche toutes les activités de cette city
        if(city != "all" and activity == "all"):
            req = c.execute("SELECT a.activity, i.name, e.nomEq, a.city from installations i, equipements e, activities a where a.city=e.city and e.numInstal=i.num and a.city=\""+city+"\";")
        #Si l'utilisateur a sélectionné une city et une activité, on affiche toutes les activités correspondant à celle sélectionnée dans la city.
        if(city != "all" and activity != "all"):
            req = c.execute("SELECT a.activity, i.name, e.nomEq, a.city from installations i, equipements e, activities a where a.city=e.city and e.numInstal=i.num and a.city=\""+city+"\" and a.activity=\""+activity+"\";")
        #Si l'utilisateur a sélectionné seulement une activité on affiche toutes les citys où l'on peut pratiquer cette activité
        if(city == "all" and activity != "all"):
            req = c.execute("SELECT \""+activity+"\", i.name, e.nomEq, a.city from installations i, equipements e, activities a where a.city=e.city and e.numInstal=i.num and a.activity=\""+activity+"\" limit 20;")
        if(city == "all" and activity == "all"):
        	req = []
        if req != []:
            list = [a for a in req]
            c.close()
            #on envoie ces données au template tmpt_correct.
            return template('tpl/tmpt_results', results=list)
        else:
            return("Veuillez rentrer au moins une ville ou une activité")

        

    except Exception as error:
        print("Unexpected error: {0}".format(error))
        return("erreur")


#on lance le serveur sur localhost, sur le port choisi
run(host='localhost', port=8182)
