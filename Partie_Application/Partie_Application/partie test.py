#VARIABLES

nbFamilles = int(input())
nbMembres = int(input())

liste = []
compteur_min = nbMembres

for i in range(nbFamilles):
    liste.append(input())

nbCartes = int(input())
cartesDeJoseph = input()

#FONCTIONS

def nb_cartes_valides(dieux, compteur_min, Joseph):

    compteur_actuel = nbMembres

    for i in range(len(dieux)):
        if dieux[i] in Joseph:
            compteur_actuel -= 1

            #enlever le caractère trouvé
            Joseph = Joseph.replace(dieux[i], "")

    if compteur_min < compteur_actuel:
        return compteur_min
    else:
        return compteur_actuel
#CODE

for i in range(nbFamilles):
    compteur_min = nb_cartes_valides(liste[i], compteur_min, cartesDeJoseph)

print(compteur_min)

