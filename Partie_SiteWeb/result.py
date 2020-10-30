#je met tout en francais

import cgi, cgitb

#a enlever lorsque le site fonctionne
cgitb.enable()
formulaire = cgi.FieldStorage()

if formulaire.getvalue("username"):
    nom_utilisateur = formulaire.getvalue("username")

#enlever l'erreur
else:
    raise Exception("Pseudo non transmis")

print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>Ma page web</title>
</head>
<body>
    <h1>Resultats</h1>
"""

print(html)
print(f"Bonjour {nom_utilisateur} !")

html = """
    <form method="post" action="result.py">
        <p><input type="text" name="username">
        <input type="submit" value="Envoyer"></p>
    </form>
</body>
</hmtl>
"""

print(html)