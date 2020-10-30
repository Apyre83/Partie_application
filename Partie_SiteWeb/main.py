'''

coding:utf-8
MySql est le plus interessant pour mon site ! --> pour les petits site, sinon c'est postgreSql et enfin il y a sqlite mais ça jsp
pour le test je fais quand meme avec sqlite xD

la base de la base: CRUD: Create, Read, Update, Delete
'''

import sqlite3

#gerer les erreurs:
try:
    #mettre dans le try tout ce qu'il y a a faire
    connexion = sqlite3.connect("base.db")
    cursor = connexion.cursor()

    user = ("TOTO",)
    req = cursor.execute('SELECT * FROM site_users WHERE user_name = ?', user)
    #print(...)
    for row in req:
        print(row[1])

except Exception as e:
    print("[ERREUR]", e)
    connexion.rollback()

finally:
    connexion.close()




'''
#se connecter:
connexion = sqlite3.connect("base.db")

#creer le curseur:
cursor = connexion.cursor()

#print(type(connexion))
#print(type(cursor))

#ajouter une valeur a la table
new_user = (cursor.lastrowid, "Julie", 23)
cursor.execute('INSERT INTO site_users VALUES(?, ?, ?)', new_user)
connexion.commit()

#print("Nouvel utilisateur ajouté !")

#recuperer TOUT ce qu'il y a dans la liste
req = cursor.execute('SELECT * FROM site_users')

#print(req.fetchall()) #sinon req.fetchone pour en recuperer 1 seule

for row in req.fetchall():
    print(row[1])




#revenir au dernier commit si il y a eu un probleme
#connexion.rollback()
#fermer:
connexion.close()
'''