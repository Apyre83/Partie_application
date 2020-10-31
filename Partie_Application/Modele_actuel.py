#coding:utf-8

import tkinter, pygame, sys, sqlite3

#Débuter le programme
pygame.init()

#Variables

longueur = 1920
largeur = 1080
bordure = 30

couleurBordure = pygame.Color("orange")
premierPlan = pygame.Color("white")
arrierePlan = pygame.Color("black")

#Chargement des images
imageFond = pygame.image.load("Fond.jpg")
imageMenuPrincipal = pygame.transform.scale(pygame.image.load("cahier.jpg"), (longueur, largeur))
image_supprimer = pygame.transform.scale(pygame.image.load("image_supprimer.png"), (30, 30))
image_bouton_plus = pygame.transform.scale(pygame.image.load('image_bouton_plus.png'), (45, 28))

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
                    #Chaque ligne du cahier de text est séparée par une ordonnée y de 54 environ
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
        le_devoirs = devoirs[1]
        le_devoirs = ''.join(le_devoirs)
        #print(le_devoirs)
        #print(requete.fetchall())
        police = pygame.font.Font("Because I am Happy Regular.ttf", 40)
        #La police est toujours la même parce que flemme de changer ou peut être que je le ferai plus tard + afficher ce qu'il y a faire sur l'image
        texte = police.render(le_devoirs, True, pygame.Color("#000000"))
        screen.blit(texte, (x, y))

        # Afficher les icones pour supprimer
        screen.blit(image_supprimer, (875, y + 8))
        y += 54

    #Afficher l'icone pour ajouter un nouveau devoirs:
    screen.blit(image_bouton_plus, (90, y + 10))

    connexion.close()  #Ferme la connexion

def ajouter_devoirs():

    #On démarre une connexion à la table comme d'hab
    connexion = sqlite3.connect('Gerer_les_devoirs.db')
    curseur = connexion.cursor()

    #On vérifie qu'on ait bien cliqué sur la croix bleue:

    requete = curseur.execute('SELECT * FROM  les_notes')

    #print(len(requete.fetchall()))

    longueur = len(requete.fetchall())

    xMin = 101
    xMax = 126
    yMin = 109 + 54 * longueur
    yMax = 136 + 54 * longueur

    position_souris_x = pygame.mouse.get_pos()[0]
    position_souris_y = pygame.mouse.get_pos()[1]

    #print(position_souris_x, position_souris_y)
    #print(xMin, xMax, yMin, yMax)

    curseur = connexion.cursor()

    if xMin <= position_souris_x <= xMax and yMin <= position_souris_y <= yMax:

        def ecrire_devoirs(event):       #Ecriture dans la table SQL
                                                                   #Ici il faudra changer et faire une sorte de menu déroulant parce que pour les devoirs on ajoute que des maths (curseur.lastrowid, "Maths"...)
            curseur.execute("INSERT INTO les_notes (id_devoirs, A_Faire) VALUES (?, ?)", (curseur.lastrowid,  ligne_texte.get()))

            connexion.commit()      #Sauvergarder les modifications
            afficher_devoirs()          #Actualiser
            fenetre_tkinter.destroy()   #Quitter tkinter
        
    #On créer ici la fenêtre tkinter ce qu'il y a à changer
        fenetre_tkinter = tkinter.Tk()

        ligne_texte = tkinter.Entry(fenetre_tkinter, width = 30)
        ligne_texte.pack()
        fenetre_tkinter.bind('<Return>', ecrire_devoirs)

        fenetre_tkinter.mainloop()
    connexion.close()

def supprimer_devoirs():

    def confirmer_suppression():


        a_supprimer = (i[0],)
        #On supprimer le devoirs correspond à la ligne choisie
        requete.execute("DELETE FROM les_notes WHERE id_devoirs = ?", a_supprimer)
        connexion.commit()

        #On ferme la fenetre tkinter
        fenetre_tkinter.destroy()
        afficher_devoirs()


    def annuler_suppression():
        fenetre_tkinter.destroy()
    #On récupère la position de la souris
    position_souris = pygame.mouse.get_pos()
    position_souris_x = position_souris[0]
    position_souris_y = position_souris[1]

    #print(position_souris)
    #Cooordonées du premier bouton "Supprimer" (ENVIRON ce n'est pas exact)
    xMin = 878
    xMax = 900
    yMin = 110
    yMax = 134
    '''
    On créer la fenêtre tkinter afin de savoir si on veut bien supprimer le devoirs ou annuler sa suppression ||                               A CHANGER PAR UNE BELLE FENETRE :)
    Au passage on s'en fou d'ouvrir et de fermer plein de fois la table SQL ça ne réduit pas les performances !
    En dessous en démarre une connexion pour connaître le nombre de devoirs pour la boucle
    '''
    connexion = sqlite3.connect("Gerer_les_devoirs.db")
    curseur = connexion.cursor()
    requete = curseur.execute('SELECT * FROM  les_notes')

    #On démarre la boucle pour savoir si on a cliqué sur un logo poubelle
    for i in requete.fetchall(): #Permet d'avoir le nombre de devoirs (pour la boucle :) )
        if xMin <= position_souris_x <= xMax and yMin <= position_souris_y <= yMax:
            fenetre_tkinter = tkinter.Tk()

            bouton_confirmer = tkinter.Button(fenetre_tkinter, text="Confirmer la suppression ?",
                                              command=confirmer_suppression, height=10, width=20)
            bouton_annuler = tkinter.Button(fenetre_tkinter, text="Annuler la suppression ?", command=annuler_suppression,
                                            height=10, width=20)

            bouton_confirmer.pack(side="right")
            bouton_annuler.pack(side="left")

            fenetre_tkinter.mainloop()
        yMin += 54
        yMax += 54

    #On supprimer la connexion à la table SQL
    connexion.close()
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


while True:
    for event in pygame.event.get():
        # Quitter
        if event.type == pygame.QUIT:
            sys.exit()
        # clavier
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                afficher_devoirs()

        # souris
        if event.type == pygame.MOUSEBUTTONUP:
            ajouter_devoirs()
            supprimer_devoirs()
        pygame.display.flip()