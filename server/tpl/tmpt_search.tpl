<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="utf-8">
		<title>Recherche</title>
	</head>

    <body>
  		<h1>Recherche</h1>
  		Choisissez une ville ou une activité : <br/><br/>
      <form action="/search" method="POST">
        Ville :
        <select name="city">
          <option value="all">Sélectionner toutes les villes</option>
          %for x in city:
            <option value="{{x}}">{{x}}</option>
          %end
        </select>
  		Activité :
  		<select name="activity">
  			<option value="all">Sélectionner toutes les activités</option>
  			%for y in activity:
  				<option value="{{y}}">{{y}}</option>
  			%end
  		</select>

  		<input type="submit" value="Rechercher">
  	</form>
  </body>
</html>
