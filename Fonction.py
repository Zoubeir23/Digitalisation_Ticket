#Mes fonctions:

destination = "" #Initialisation de la variable destination (variable globale)
prix = 0 #Initialisation de la variable prix (variable globale)

#Creation de la fonctiom d'affichage du menu
def menu():
    '''
    Fonction qui affiche le menu
    '''
    print ("\n\
    1- Acheter un ticket\n\
    2- Acheter une carte d'abonnement\n\
    3- Quitter\n")
    

#Creation de la fonction d'affichage des zones
def zones():
    '''
    Fonction qui affiche les zones
    '''
    print("\n\
    1- Zone 1\n\
    2- Zone 2\n\
    3- Zone 3\n")
#Creation de la fonction d'affichage de la Zone1
def Zone1():
    '''
    Fonction qui affiche les zones
    '''
    print("Veuillez choisir une zone : ")
    print("\n\
    - Keur Massar\n\
    - Yumbeule\n\
    - Apix\n")

#Creation de la fonction d'affichage de la Zone2
def Zone2():
    '''
    Fonction qui affiche les zones
    '''
    print("Veuillez choisir une zone : ")
    print("\n\
    - Parcelle\n\
    - Dior\n\
    - Soprim\n\
    - Pate d'oie\n\
    - Gard Yoff\n")

#Creation de la fonction d'affichage de la Zone3
def Zone3():
    '''
    Fonction qui affiche les zones
    '''
    print("\n\
    - Ngor\n\
    - Ouakam\n\
    - Yoff\n\
    - Foire\n\
    - Coloban\n\
    - Ucad\n")

#Creation de la fonction Zone_1
def Zone_1(Nom):
    '''
    Fonction qui vérifie la ligne de 
    destination et affiche le prix du ticket
    '''
    global destination
    global prix
    Nom = Nom.lower()
    if Nom == "keur massar":
        print(f"Ticket à 250 CFA")
        destination = Nom
        prix = 250
    elif Nom == "yumbeule":
        print(f"Ticket à 300 CFA")
        destination = Nom
        prix = 300
    elif Nom == "apix":
        print(f"Ticket à 350 CFA")
        destination = Nom
        prix = 350
    else:
        print(f"{Nom} n'est pas disponible !")
#Creation de la fonction Zone_2
def Zone_2(Nom):
    '''
    Fonction qui vérifie la ligne de 
    destination et affiche le prix du ticket
    '''
    global destination
    global prix
    Nom = Nom.lower()
    if Nom == "parcelle":
        print(f"Ticket à 200 CFA")
        destination = Nom
        prix = 200
    elif Nom == "dior":
        print(f"Ticket à 150 CFA")
        destination = Nom
        prix = 150
    elif Nom == "soprim":
        print(f"Ticket à 250 CFA")
        destination = Nom
        prix = 250
    elif Nom == "pate d'oie":
        print(f"Ticket à 350 CFA")
        destination = Nom
        prix = 350
    elif Nom == "gard yoff":
        destination = Nom
        prix = 400
        print(f"Ticket à 400 CFA")   
    else:
        print(f"{Nom} n'est pas disponible !")
#Creation de la fonction Zone_3
def Zone_3(Nom):
    '''
    Fonction qui vérifie la ligne de 
    destination et affiche le prix du ticket
    '''
    global destination
    global prix
    Nom = Nom.lower()
    if Nom == "ngor":
        print(f"Ticket à 200 CFA")
        destination = Nom
        prix = 200
    elif Nom == "ouakam":
        print(f"Ticket à 500 CFA")
        destination = Nom
        prix = 500
    elif Nom == "yoff":
        print(f"Ticket à 250 CFA")
        destination = Nom
        prix = 250
    elif Nom == "foire":
        print(f"Ticket à 300 CFA")
        destination = Nom
        prix = 300
    elif Nom == "coloban":
        print(f"Ticket à 450 CFA")
        destination = Nom
        prix = 450
    elif Nom == "ucad":
        print(f"Ticket à 400 CFA")
        destination = Nom
        prix = 400
    else:
        print(f"{Nom} n'est pas disponible !")

#Creation de la fonction vérification de la zone
def verife_zone1(x):
    '''
    Fonction qui vérifie la ligne de 
    destination et affiche le prix du ticket
    '''
    global prix
    while True:
        destination = input("Veuillez choisir une ligne de destination : ")
        Zone_1(destination)
        if prix != 0:  # Si un prix valide a été défini
            break

def verife_zone2(x):
    '''
    Fonction qui vérifie la ligne de 
    destination et affiche le prix du ticket
    '''
    global prix
    while True:
        destination = input("Veuillez choisir une ligne de destination : ")
        Zone_2(destination)
        if prix != 0:
            break

def verife_zone3(x):
    '''
    Fonction qui vérifie la ligne de 
    destination et affiche le prix du ticket
    '''
    global prix
    while True:
        destination = input("Veuillez choisir une ligne de destination : ")
        Zone_3(destination)
        if prix != 0:
            break
