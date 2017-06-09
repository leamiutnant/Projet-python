import sqlite3

from libs.bottle import get, post, request, route, template, run

"""
Serveur qui va permettre d'intéragir avec les données de la bd et celles qu'on utilise dans les templates,
en utilisant la librairie bottle.
"""

#Lancement de la page où l'on doit sélectionner une city et/ou une activité
@route('/home')
def home():
    conn = sqlite3.connect("../bddata/database.db")
    c = conn.cursor()
    city = c.execute("SELECT a.city from activities a;")
    l_city = [a for a in city]
    c.close()

    conn = sqlite3.connect("../bddata/database.db")
    c = conn.cursor()
    activity = c.execute("SELECT a.activity from activities a;")
    l_activity = [a for a in activity]
    c.close()
    return template('tpl/tmpt_search', city = l_city, activity = l_activity)

#méthode qui fait les requêtes sql pour afficher les résultats en fonction de la recherche effectuée.
@post('/research')
def research():
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
            list = [a for a in req]
            #on envoie ces données au template tmpt_correct.
            return template('tpl/tmpt_results', results=list)
        #Si l'utilisateur a sélectionné une city et une activité, on affiche toutes les activités correspondant à celle sélectionnée dans la city.
        if(city != "all" and activity != "all"):
            req = c.execute("SELECT a.activity, i.name, e.nomEq, a.city from installations i, equipements e, activities a where a.city=e.city and e.numInstal=i.num and a.city=\""+city+"\" and a.activity=\""+activity+"\";")
            list = [a for a in req]
            #on envoie ces données au template tmpt_correct.
            return template('tpl/tmpt_results', results=list)
        #Si l'utilisateur a sélectionné seulement une activité on affiche toutes les citys où l'on peut pratiquer cette activité
        if(city == "all" and activity != "all"):
            req = c.execute("SELECT a.city, i.name, e.nomEq from installations i, equipements e, activities a where a.city=e.city and e.numInstal=i.num and a.activity=\""+activity+"\";")
            list = [a for a in req]
            #on envoie ces données au template tmpt_correct.
            return template('tpl/tmpt_results', results=list)

        c.close()

    except Exception as error:
        print("Unexpected error: {0}".format(error))
        return("erreur")


#on lance le serveur sur localhost, sur le port choisi
run(host='localhost', port=8182)
