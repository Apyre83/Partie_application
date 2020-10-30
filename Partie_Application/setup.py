#coding:utf-8
import tkinter as tk, pygame, sys, sqlite3

#Débuter le programme
pygame.init()

#Variables

longueur = 1920
largeur = 1080
bordure = 30

couleurBordure = pygame.Color("orange")
premierPlan = pygame.Color("white")
arrierePlan = pygame.Color("black")

#Les images
imageFond = pygame.image.load("Fond.jpg")
imageMenuPrincipal = pygame.transform.scale(pygame.image.load("cahier.jpg"), (longueur, largeur))
image_supprimer = pygame.transform.scale(pygame.image.load("image_supprimer.png"), (30, 30))

accueil = True
alpha = 1

# Fonctions:
def menu_principal():
    global imageMenuPrincipal
    screen.blit(imageMenuPrincipal, (0, 0))


def dialogue_debut():
    screen = pygame.display.set_mode((longueur, largeur), pygame.RESIZABLE)

    pygame.draw.rect(screen, premierPlan, pygame.Rect(0, 0, longueur, bordure))
    screen.blit(imageFond, (0, 0))

    police = pygame.font.Font("jd_digital.ttf", 72)
    texte = police.render("Coucou ! J'éspère que tu as passé une merveille !", True, pygame.Color("#3B2A27"))
    screen.blit(texte, (50, 50))
    texte = police.render(" journée Senpai !! Allons faire nos devoirs ", True, pygame.Color("#3B2A27"))
    screen.blit(texte, (50, 100))
    texte = police.render("ensemble, c'est important, plus tard tu pourras ", True, pygame.Color("#3B2A27"))
    screen.blit(texte, (50, 150))
    texte = police.render("me recréer !", True, pygame.Color("#3B2A27"))
    screen.blit(texte, (50, 200))

'''
                                                                                                                                                                                                                                            A voir pour le \n
police = pygame.font.Font("jd_digital.ttf", 72)
texte = police.render("Coucou ! J'éspère que tu as passé u"
                      "ne merveilleuse journée Senpai !\nAllons faire no"
                      "s devoirs ensemble, c'est important, plus tard"
                      " tu\npourras me recréer rappelles-toi !", True,
                      pygame.Color("#3B2A27"))
screen.blit(texte, (50, 150))
'''

def afficher_devoirs():

    x = 100
    y = 97

    #Etablir la connexion avec le serveur
    menu_principal()
    connexion = sqlite3.connect("Gerer_les_devoirs.db")
    #Créer le curseur et donc la requete pour récupérer les infos
    curseur = connexion.cursor()
    requete = curseur.execute('SELECT * FROM  les_notes')
    #Les affichier avec "devoirs à faire ", "en", "matière"
    for devoirs in requete.fetchall():
        #Récupérer le devoirs
        le_devoirs = devoirs[2], "en", devoirs[1]
        le_devoirs = ' '.join(le_devoirs)
        #print(le_devoirs)
        #print(requete.fetchall())
        police = pygame.font.Font("Because I am Happy Regular.ttf", 40)
        #La police est toujours la même parce que flemme de changer ou peut être que je le ferai plus tard + afficher ce qu'il y a faire sur l'image
        texte = police.render(le_devoirs, True, pygame.Color("#000000"))
        screen.blit(texte, (x, y))

        # Afficher les icones pour supprimer
        screen.blit(image_supprimer, (875, y + 8))

        y += 54







    #Fermer
    connexion.close()


def ajouter_devoirs():
    pass

def supprimer_devoirs():
    pass

#Creer la fenêtre
screen = pygame.display.set_mode((longueur, largeur), pygame.RESIZABLE)

pygame.draw.rect(screen, premierPlan, pygame.Rect(0, 0, longueur, bordure))
screen.blit(imageFond, (0, 0))

#Boucles:
afficher_devoirs()
while accueil == True:
    dialogue_debut()
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            sys.exit()

        if evenement.type == pygame.KEYDOWN:
            if evenement.key == pygame.K_RETURN:
                afficher_devoirs()
                accueil = False

        pygame.display.flip()
                                                                                   # A CHAQUE FOIS QUIL Y A MARQUE MENU PRINCIPALE() IL FAUDRA LE CHANGER UNE FOIS QUE JAURAI FINI

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
                ajouter_devoirs()

        # souris
        if event.type == pygame.MOUSEBUTTONUP:
            supprimer_devoirs()

        pygame.display.flip()
