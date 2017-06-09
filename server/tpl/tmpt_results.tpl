<!DOCTYPE HTML>
<html>
	<head>
		<meta charset="utf-8">
		<title>Résultats</title>
	</head>

	<body>
		<h1>Resultats de votre recherche</h1>

		<table>
			<tr><th>Activité</th><th>Installation</th><th>Equipement</th><th>Ville</th></tr>
			%for x in results:
				<tr>
					<td>{{x[0]}}</td>
					<td>{{x[1]}}</td>
					<td>{{x[2]}}</td>
					<td>{{x[3]}}</td>
					<td>{{x[4]}}</td>

				</tr>
			%end
		</table>

	</body>
</html>
