import Fonction

Quiter = True

while Quiter:
    #Affichage du menu
    Fonction.menu()
    #Sélection de l'option

    print("******"*20)

    #Vérification de l'option
    option = int(input("Veuillez choisir une option : "))
    if option == 1:
        #Affichage des zones
        Fonction.zones()
        print("Achat d'un ticket")

        #Sélection de la zone
        zone = int(input("Veuillez choisir une zone : "))
        print("******"*20)

        #Vérification de la zone
        if zone == 1:
            Fonction.Zone1()
            print("******"*20)
            Fonction.verife_zone1(zone)
            paiement = int(input("Veuillez saisir un montant de paiement : "))
            if paiement >= 2000 or paiement < Fonction.prix:
                print(f"Le montant doit être entre {Fonction.prix} et 2000 CFA")
            else:
                monnaie = paiement - Fonction.prix
                print(f"Monnaie à rendre : {monnaie} CFA")
                print("******"*20)
                print(f"Ticket : {Fonction.destination}, Prix : {Fonction.prix} CFA, Monnaie à rendre : {monnaie} CFA")
            print("******"*20)
        elif zone == 2:
            Fonction.Zone2()
            print("******"*20)
            Fonction.verife_zone2(zone)
            paiement = int(input("Veuillez saisir un montant de paiement : "))
            if paiement >= 2000 or paiement < Fonction.prix:
                print(f"Le montant doit être entre {Fonction.prix} et 2000 CFA")
            else:
                monnaie = paiement - Fonction.prix
                print(f"Monnaie à rendre : {monnaie} CFA")
                print("******"*20)
                print(f"Ticket : {Fonction.destination}, Prix : {Fonction.prix} CFA, Monnaie à rendre : {monnaie} CFA")
            print("******"*20)
        elif zone == 3:
            Fonction.Zone3()
            print("******"*20)
            Fonction.verife_zone3(zone)
            print("******"*20)
            paiement = int(input("Veuillez saisir un montant de paiement : "))
            if paiement >= 2000 or paiement < Fonction.prix:
                print(f"Le montant doit être entre {Fonction.prix} et 2000 CFA")
            else:
                monnaie = paiement - Fonction.prix
                print(f"Monnaie à rendre : {monnaie} CFA")
                print("******"*20)
                print(f"Ticket : {Fonction.destination}, Prix : {Fonction.prix} CFA, Monnaie à rendre : {monnaie} CFA")
            print("******"*20)
        else:
            print("Zone non disponible !")

        #Vérification de la variable quitter
        Quiter = bool((input("Voulez-vous quitter ? (True = oui, False = non) : ")))
        print("******"*20)