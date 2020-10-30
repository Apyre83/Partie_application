import pygame, sys, random
import tkinter

pygame.init()

# Variables:

couleurBordure = pygame.Color("orange")
premierPlan = pygame.Color("white")
arrierePlan = pygame.Color("black")

longueur = 1920
largeur = 1080
bordure = 30

imageFond = pygame.image.load("Fond.jpg")
imageMenuPrincipal = pygame.image.load("cahier.jpg")
image_supprimer = pygame.image.load("image_supprimer.png")

accueil = True

# je ne sais pas ou le mettre:

image_supprimer = pygame.transform.scale(image_supprimer, (30, 30))


# FONCTIONS:

def menu_principal():
    global imageMenuPrincipal
    imageMenuPrincipal = pygame.transform.scale(imageMenuPrincipal, (longueur, largeur))
    screen.blit(imageMenuPrincipal, (0, 0))


def afficher_devoirs():
    # on appelle menu_principal pour éviter de faire des "tampons"
    menu_principal()

    x = 100
    y = 97
    longueurMax = 600
    police = pygame.font.Font("Because I am Happy Regular.ttf", 40)

    with open("devoirs.txt", "r") as fic:
        # 44
        nombre_lignes = 0
        for line in fic:
            nombre_lignes += 1

        liste = []
        fic.seek(0)

        for i in range(nombre_lignes):
            line = fic.readline()
            liste.append(line)

        for i in range(len(liste) - 1):
            liste[i] = liste[i].rstrip("\n")

        compteur_de_vide = 0
        for i in range(len(liste)):
            if liste[i - compteur_de_vide] == "" or liste[i - compteur_de_vide] == "\n":
                print(liste)
                liste.pop(i - compteur_de_vide)
                compteur_de_vide += 1



        for i in range(len(liste)):

            police = pygame.font.Font("Because I am Happy Regular.ttf", 40)



            if len(liste[i]) > 40:
                police = pygame.font.Font("Because I am Happy Regular.ttf", 35)
                y += 5
            if len(liste[i]) > 50:
                police = pygame.font.Font("Because I am Happy Regular.ttf", 30)
                y += 7
            if len(liste[i]) > 60:
                police = pygame.font.Font("Because I am Happy Regular.ttf", 25)
                y += 1
            texte = police.render(liste[i], True, pygame.Color("#000000"))

            screen.blit(texte, (x, y))

            y += 54
            if len(liste[i]) > 60:
                y += 1
            elif len(liste[i]) > 50:
                y -= 7
            elif len(liste[i]) > 40:
                y -= 5
        y = 159

        for i in range(len(liste) - 1):
            screen.blit(image_supprimer, (875, y))
            y += 54


# on demande la valeur de saisir les devoirs qu'il doit faire
def demander_devoirs():
    def get_entry(event):
        devoirs_a_ajouter = ligne_texte.get()
        with open("devoirs.txt", "a") as fic:
            fic.write("\n" + devoirs_a_ajouter)
        afficher_devoirs()
        root.destroy()

    root = tkinter.Tk()

    ligne_texte = tkinter.Entry(root, width=30)
    ligne_texte.pack()
    root.bind('<Return>', get_entry)

    root.mainloop()


def supprimer_devoirs():
    # position de la souris

    def confirmer_suppression():
        with open("devoirs.txt", "r") as fic:

            liste = []

            for i in range(nombre_lignes):
                line = fic.readline()
                liste.append(line)

        with open("devoirs.txt", "w") as fic:
            for i in range(len(liste) - 1):
                liste[i] = liste[i].rstrip("\n")


            liste.pop(ligne_a_supprimer+1)

            for i in range(nombre_lignes - 1):
                if liste[i] != "":
                    fic.write(liste[i] + "\n")

        root.destroy()
        afficher_devoirs()
    def annuler_suppression():
        root.destroy()

    position_souris = pygame.mouse.get_pos()
    position_souris_x = position_souris[0]
    position_souris_y = position_souris[1]
    ligne_a_supprimer = 0

    xMin = 875
    xMax = 904
    yMin = 161
    yMax = 187

    # Recuperer le nombre de lignes
    with open("devoirs.txt", "r") as fic:
        nombre_lignes = 0
        for line in fic:
            nombre_lignes += 1

    for i in range(nombre_lignes - 1):
        # souris sur l'icone poubelle
        if xMin <= position_souris_x <= xMax and yMin <= position_souris_y <= yMax:
            root = tkinter.Tk()

            bouton_confirmer = tkinter.Button(root, text="Confirmer la suppression ?",
                                              command=confirmer_suppression, height=10, width=20)
            bouton_annuler = tkinter.Button(root, text="Annuler la suppression ?", command=annuler_suppression,
                                            height=10, width=20)

            bouton_confirmer.pack(side="right")
            bouton_annuler.pack(side="left")

            root.mainloop()

        ligne_a_supprimer += 1
        yMin += 54
        yMax += 54



# Accueil --> aller au menu principal

screen = pygame.display.set_mode((longueur, largeur), pygame.RESIZABLE)

pygame.draw.rect(screen, premierPlan, pygame.Rect(0, 0, longueur, bordure))
screen.blit(imageFond, (0, 0))

police = pygame.font.Font("jd_digital.ttf", 72)
texte = police.render("Coucou ! J'éspère que tu as passé une merveille journée Senpai !", True, pygame.Color("#3B2A27"))
screen.blit(texte, (50, 50))
texte = police.render("Allons faire nos devoirs ensemble, c'est important, plus tard tu ", True, pygame.Color("#3B2A27")
                      )
screen.blit(texte, (50, 100))
texte = police.render("pourras me recréer !", True, pygame.Color("#3B2A27"))
screen.blit(texte, (50, 150))

while accueil == True:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            sys.exit()

        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_RETURN:
                afficher_devoirs()
                accueil = False

        pygame.display.flip()

# Fin accueil
# Lister les devoirs


while True:
    for event in pygame.event.get():
        # Quitter
        if event.type == pygame.QUIT:
            sys.exit()
        # clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                afficher_devoirs()

            if event.key == pygame.K_SPACE:
                demander_devoirs()
        # souris
        if event.type == pygame.MOUSEBUTTONUP:
            supprimer_devoirs()

        pygame.display.flip()

