# Instalations sportives des Pays de la Loire
### Base de donnees :
J'ai d'abord créé une base de données nommée database.bd située dans le dossier bddata . Ensuite avec le fichier bd.py je créer mes trois tables : activities, equipements, installations. J'ai rempli ces tables grace aux données que j'ai récupéré dans les fichiers csv (bddata>csv).
Données que j'ai choisi dans le fichier csv_parser, puis dans ce fichier je créer un objet d'Activity, d'Equipement ou d'Installation, qui sont trois classes créées dans leur fichier respectif (activities.py,...).

### Serveur :
Le serveur est géré par la librairie bottle.
Dans le dossier server on trouve d'abord le fichier qui permet de lancer l'application, puis le dossier tpl avec les templates dont on a besoin, ainsi que le dossier libs qui contient la librairie bottle.
Le fichier server.py appelle les données pour les envoyer dans un template qui va les afficher sur une page web, ensuite il créer les requetes en fonction des données sélectionnées dans le premier template et il envoie vers un deuxième template qui affiche les résultats en fonction des données sélectionnées.

### Fonctionnement :
Pour lancer la base de données il faut ouvrir un terminal et aller dans le dossier bddata puis taper la commande python3 bd.py;
Pour lancer l'application il faut lancer le serveur : ouvrir un terminal et aller dans le dossier server qui contient le fichier server.py puis taper la commande python3 server.py
Ensuite, ouvrez un naviguateur et entrez l'adresse suivante : http://localhost:8182/home
Enfin, vous devriez voir s'afficher la première page qui vous propose de sélectionner une activité et/ou un sport.
Une fois votre choix fait, il vous suffit de cliquer sur rechercher et vous allez etre redirigé vers une seconde page où vont s'afficher les résultats en fonction de votre recherche. Vous pouvez également cliquer sur un lien vous permettant de retourner sur la première page pour pouvoir effectuer une nouvelle recherche.

### Problèmes :
Le problème d'affichage des villes et des activités est du au fait qu'on fasse une liste pour parcourir le cursor, mais je n'ai pas réussi à le gérer.
