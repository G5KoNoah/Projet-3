#on definit une fonction input qui récupere l'entree d'un joueur


#on definit une fonction morpion
def morpion(nombreJoueur):
    #on initialise un tableau avec 3 listes qui contiennent 3 caracteres vides  
    tab = [[" □ " for i in range(3)] for j in range(3)]
    noWin = True
    nbTour = 0
    vainqueur = "Le vainqueur est : "
    nomJoueurA = input("Le nom du joueur 1 : \n")
    change = False
    #si il n'y a qu'un joueur
    if nombreJoueur == 1 :
        #alors on determine nomJoueurB a "IA"
        nomJoueurB = "IA"
    #sinon
    else :
        #on assigne a nomJoueurB le string du retour de l'execution de la fonction input
        nomJoueurB = input("Le nom du joueur 2 : \n")

    symboleJoueurA = input("Symbole du joueur 1 : \n X ou O \n")

    while symboleJoueurA != "X" and symboleJoueurA != "O" :
        symboleJoueurA = input("Veuillez resaisir le symbole du joueur 1 : \n")

    if symboleJoueurA == "X" :
        symJouA = " X "
        symJouB = " O "
    else :
        symJouB = " X "
        symJouA = " O "

    for i in tab:
        for j in i:
            print(j, end="")
        print()
        
    while noWin:
        nbTour = nbTour + 1 
        print("choixJoueur 1 : \n")
        while change == False:
            ligne = input("ligne : \n")
            while ligne !="1" and ligne !="2" and ligne !="3" :
                ligne = input("Veuillez resaisir la ligne : \n")

            colonne = input("Colonne : \n")
            while colonne !="1" and colonne !="2" and colonne !="3" :
                ligne = input("Veuillez resaisir la colonne : \n")
            lig = int(ligne)-1
            col = int(colonne)-1
            if tab[lig][col] == " □ " :
                change = True
            else :
                print("Case dejà modifiée")

        tab[lig][col] = symJouA
        change = False

        #ligne
        for i in range(0,3):
            if tab[i][0]==symJouA and tab[i][1]==symJouA and tab[i][2]==symJouA :
                for i in tab:
                    for j in i:
                        print(j, end="")
                    print()
                return vainqueur + nomJoueurA
        
        
        #colonne
        for i in range(0,3):
            if tab[0][i]==symJouA and tab[1][i]==symJouA and tab[2][i]==symJouA :
                for i in tab:
                    for j in i:
                        print(j, end="")
                    print()
                return vainqueur + nomJoueurA


        
        #diagonale
        if tab[0][0]==symJouA and tab[1][1]==symJouA and tab[2][2]==symJouA or tab[2][0]==symJouA and tab[1][1]==symJouA and tab[0][2]==symJouA :
            for i in tab:
                for j in i:
                    print(j, end="")
                print()
            return vainqueur + nomJoueurA


        for i in tab:
            for j in i:
                print(j, end="")
            print()
        
        if nbTour == 5 :
            noWin = False

        print("choixJoueur 2 : \n")
        
        while change == False :
            ligne = input("ligne : \n")
            while ligne !="1" and ligne !="2" and ligne !="3" :
                ligne = input("Veuillez resaisir la ligne : \n")
            colonne = input("Colonne : \n")
            while colonne !="1" and colonne !="2" and colonne !="3" :
                ligne = input("Veuillez resaisir la colonne : \n")
            lig = int(ligne)-1
            col = int(colonne)-1
            if tab[lig][col] == " □ " :
                    change = True
            else :
                print("Case dejà modifiée")
        tab[lig][col] = symJouB
        change = False

        #ligne
        for i in range(0,3):
            if tab[i][0]==symJouB and tab[i][1]==symJouB and tab[i][2]==symJouB :
                for i in tab:
                    for j in i:
                        print(j, end="")
                    print()
                return vainqueur + nomJoueurB
        
        
        #colonne
        for i in range(0,3):
            if tab[0][i]==symJouB and tab[1][i]==symJouB and tab[2][i]==symJouB :
                for i in tab:
                    for j in i:
                        print(j, end="")
                    print()
                return vainqueur + nomJoueurB    
    
        #diagonale
        if  tab[0][0]==symJouB and tab[1][1]==symJouB and tab[2][2]==symJouB or tab[2][0]==symJouB and tab[1][1]==symJouB and tab[0][2]==symJouB:
            for i in tab:
                for j in i:
                    print(j, end="")
                print()
            return vainqueur + nomJoueurB

            
        for i in tab:
            for j in i:
                print(j, end="")
            print()
        
        if nbTour == 6 :
            noWin = False
    return "Egalite"

demande = input("Voulez-vous jouer au morpion ? Yes or No \n")
while demande == "Yes":
    print(morpion(2))
    demande = input("Voulez-vous rejouer au morpion ? Yes or No \n")