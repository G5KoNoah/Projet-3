#on definit une fonction input qui récupere l'entree d'un joueur

#on definit une fonction display qui renvoie un affichage d'une liste de liste en tableau

#on definit une fonction morpion avec comme parametre le nombreJoueur 
def morpion(nombreJoueur):
    #on initialise un tableau avec 3 listes qui contiennent 3 caracteres vides □
    tab = [[" □ " for i in range(3)] for j in range(3)]
    #on initialise noWin a True
    noWin = True
    #on initialise nbTour a 0
    nbTour = 0
    #on definit vainqueur au string "Le vainqueur est : "
    vainqueur = "Le vainqueur est : "
    #on assigne nomJoueurA le string du retour de la fonction input 
    nomJoueurA = input("Le nom du joueur 1 : \n")
    #on initialise change a False
    change = False
    #si il n'y a qu'un joueur
    if nombreJoueur == 1 :
        #alors on determine nomJoueurB a "IA"
        nomJoueurB = "IA"
        config=""
    #sinon
    else :
        #on assigne a nomJoueurB le string du retour de l'execution de la fonction input
        nomJoueurB = input("Le nom du joueur 2 : \n")

    #on assigne symboleJoueurA le string du retour de la fonction input 
    symboleJoueurA = input("Symbole du joueur 1 : \n X ou O \n")

    #tant que symboleJoueurA est different de "X" et "O" 
    while symboleJoueurA != "X" and symboleJoueurA != "O" :
        #alors on reassigne  symboleJoueurA le string du retour de la fonction input 
        symboleJoueurA = input("Veuillez resaisir le symbole du joueur 1 : \n")

    #si symboleJoueurA est egal a "X"
    if symboleJoueurA == "X" :
        #alors
        #on initialise symJouA a " X "
        symJouA = " X "
        #on initialise symJouB a " O "
        symJouB = " O "
    #sinon
    else :
        #alors
        #on initialise symJouA a " O "
        symJouA = " O "
        #on initialise symJouB a " X "
        symJouB = " X "
        
    #on execute la fonction display
    for i in tab:
        for j in i:
            print(j, end="")
        print()

    #tant que noWIn est vrai  
    while noWin:
        #on incremente nbTour de 1
        nbTour = nbTour + 1 
        #on affiche le string "Choix du joueur 1 :"
        print("Choix du joueur 1 : \n")
        #tant que change est faux
        while change == False:
            #alors 
            #on assigne ligne le string du retour de la fonction input
            ligne = input("ligne : \n")
            #tant que ligne est different de 1, de 2 et de 3
            while ligne !="1" and ligne !="2" and ligne !="3" :
                #alors on assigne ligne au string du retour de la fonction input
                ligne = input("Veuillez resaisir la ligne : \n")

            #on assigne colonne le string du retour de la fonction input
            colonne = input("Colonne : \n")
            #tant que colonne est different de 1, de 2 et de 3
            while colonne !="1" and colonne !="2" and colonne !="3" :
                #alors on assigne colonne au string du retour de la fonction input
                ligne = input("Veuillez resaisir la colonne : \n")
            #on definit lig a l'entier de ligne en retirant 1
            lig = int(ligne)-1
            #on definit col a l'entier de colonne en retirant 1
            col = int(colonne)-1
            #si l'element du tableau ayant comme indice lig et col est egal a □ 
            if tab[lig][col] == " □ " :
                #alors on definit change a vrai
                change = True
            else :
            #sinon
                #alors on affiche "Case deja modifiee"
                print("Case dejà modifiée")
        #on definit l'element du tableau ayant comme indice lig et col a symJouA
        tab[lig][col] = symJouA
        #on definit change a false
        change = False

        """ligne et colonne"""
        #pour i chaque valeur de 0 a 3
        for i in range(0,3):
            #alors
            #si les elements d'une ligne ou d'une colonne sont egales a symJouA 
            if tab[i][0]==symJouA and tab[i][1]==symJouA and tab[i][2]==symJouA or tab[0][i]==symJouA and tab[1][i]==symJouA and tab[2][i]==symJouA :
                #alors 
                # on appelle la fonction display
                for i in tab:
                    for j in i:
                        print(j, end="")
                    print()
                #on retourne les string vainqueur et nomJoueurA
                return vainqueur + nomJoueurA
           
        """diagonale"""
        #  si les elements des diagonales sont egales a symJouA 
        if tab[0][0]==symJouA and tab[1][1]==symJouA and tab[2][2]==symJouA or tab[2][0]==symJouA and tab[1][1]==symJouA and tab[0][2]==symJouA :
            #alors 
            # on appelle la fonction display
            for i in tab:
                for j in i:
                    print(j, end="")
                print()
            #on retourne les string vainqueur et nomJoueurA
            return vainqueur + nomJoueurA

        #on appelle la fonction display
        for i in tab:
            for j in i:
                print(j, end="")
            print()
        
        #si nbTour est egal a 5
        if nbTour == 5 :
            #on retourne "Egalite"
            return "Egalite"

        #on affiche "Choix du joueur 2 :"
        print("Choix du joueur 2 : \n")

        if nomJoueurB=="IA" :
            
            for i in range(0,3):
                for j in range(0,3) :
                    if tab[i][j]== " □ ":
                        lig=i
                        col=j

            if nbTour==1:
                if tab[0][0]==symJouA or tab[0][2]==symJouA or tab[2][0]==symJouA or tab[2][2]==symJouA :
                    lig=1
                    col=1
                    config="coin"
                if tab[1][1]==symJouA:
                    lig=0
                    col=0
                    config="centre"
                if tab[0][1]==symJouA or tab[1][0]==symJouA or tab[1][2]==symJouA or tab[2][1]==symJouA:
                    lig=1
                    col=1
                    config="bord"
            
            if nbTour==2:
                if config=="coin":
                    if tab[0][0]==symJouA   :
                        if tab[2][2]==symJouA:
                            lig =2
                            col=1
                        if tab[2][1]==symJouA :
                            lig=2
                            col=0
                        if tab[1][2]==symJouA :
                            lig=0
                            col=2
                    elif tab[0][2]==symJouA :
                        if tab[2][0]==symJouA:
                            lig =2
                            col=1
                        if tab[2][1]==symJouA :
                            lig=2
                            col=2
                        if tab[1][0]==symJouA :
                            lig=0
                            col=0
                    elif tab[2][0]==symJouA :
                        if tab[0][2]==symJouA:
                            lig =0
                            col=1
                        if tab[0][1]==symJouA :
                            lig=0
                            col=0
                        if tab[1][2]==symJouA :
                            lig=2
                            col=2
                    elif tab[2][2]:
                        if tab[0][0]==symJouA:
                            lig =0
                            col=1
                        if tab[0][1]==symJouA :
                            lig=0
                            col=2
                        if tab[1][0]==symJouA :
                            lig=2
                            col=0
                

            for i in range(0,3):
                if tab[i][0]==symJouA and tab[i][1]==symJouA and tab[i][2]==" □ ":
                    lig=i
                    col=2
                if tab[i][0]==symJouA and tab[i][2]==symJouA and tab[i][1]==" □ ":
                    lig=i
                    col=1
                if tab[i][1]==symJouA and tab[i][2]==symJouA and tab[i][0]==" □ ":
                    lig=i
                    col=0
                if tab[0][i]==symJouA and tab[1][i]==symJouA and tab[2][i]==" □ ":
                    lig=2
                    col=i
                if tab[0][i]==symJouA and tab[2][i]==symJouA and tab[1][i]==" □ ":
                    lig=1
                    col=i
                if tab[1][i]==symJouA and tab[2][i]==symJouA and tab[0][i]==" □ ":
                    lig=0
                    col=i
            

            if tab[0][0]==symJouA and tab[1][1]==symJouA and tab[2][2]==" □ ":
                lig=2
                col=2 
            if tab[0][0]==symJouA and tab[2][2]==symJouA and tab[1][1]==" □ ":
                lig=1
                col=1 
            if tab[2][2]==symJouA and tab[1][1]==symJouA and tab[0][0]==" □ ":
                lig=0
                col=0
            if tab[0][2]==symJouA and tab[1][1]==symJouA and tab[2][0]==" □ ":
                lig=2
                col=0 
            if tab[0][2]==symJouA and tab[2][0]==symJouA and tab[1][1]==" □ ":
                lig=1
                col=1 
            if tab[1][1]==symJouA and tab[2][0]==symJouA and tab[0][2]==" □ ":
                lig=0
                col=2

            for i in range(0,3):
                if tab[i][0]==symJouB and tab[i][1]==symJouB and tab[i][2]==" □ ":
                    lig=i
                    col=2
                if tab[i][0]==symJouB and tab[i][2]==symJouB and tab[i][1]==" □ ":
                    lig=i
                    col=1
                if tab[i][1]==symJouB and tab[i][2]==symJouB and tab[i][0]==" □ ":
                    lig=i
                    col=0
                if tab[0][i]==symJouB and tab[1][i]==symJouB and tab[2][i]==" □ ":
                    lig=2
                    col=i
                if tab[0][i]==symJouB and tab[2][i]==symJouB and tab[1][i]==" □ ":
                    lig=1
                    col=i
                if tab[1][i]==symJouB and tab[2][i]==symJouB and tab[0][i]==" □ ":
                    lig=0
                    col=i
            

            if tab[0][0]==symJouB and tab[1][1]==symJouB and tab[2][2]==" □ ":
                lig=2
                col=2 
            if tab[0][0]==symJouB and tab[2][2]==symJouB and tab[1][1]==" □ ":
                lig=1
                col=1 
            if tab[2][2]==symJouB and tab[1][1]==symJouB and tab[0][0]==" □ ":
                lig=0
                col=0
            if tab[0][2]==symJouB and tab[1][1]==symJouB and tab[2][0]==" □ ":
                lig=2
                col=0 
            if tab[0][2]==symJouB and tab[2][0]==symJouB and tab[1][1]==" □ ":
                lig=1
                col=1 
            if tab[1][1]==symJouB and tab[2][0]==symJouB and tab[0][2]==" □ ":
                lig=0
                col=2  

        #tant que change est faux
        else :
            #tant que change est faux
            while change == False:
                #alors 
                #on assigne ligne le string du retour de la fonction input
                ligne = input("ligne : \n")
                #tant que ligne est different de 1, de 2 et de 3
                while ligne !="1" and ligne !="2" and ligne !="3" :
                    #alors on assigne ligne au string du retour de la fonction input
                    ligne = input("Veuillez resaisir la ligne : \n")

                #on assigne colonne le string du retour de la fonction input
                colonne = input("Colonne : \n")
                #tant que colonne est different de 1, de 2 et de 3
                while colonne !="1" and colonne !="2" and colonne !="3" :
                    #alors on assigne colonne au string du retour de la fonction input
                    ligne = input("Veuillez resaisir la colonne : \n")
                #on definit lig a l'entier de ligne en retirant 1
                lig = int(ligne)-1
                #on definit col a l'entier de colonne en retirant 1
                col = int(colonne)-1
                #si l'element du tableau ayant comme indice lig et col est egal a □ 
                if tab[lig][col] == " □ " :
                    #alors on definit change a vrai
                    change = True
                else :
                #sinon
                    #alors on affiche "Case deja modifiee"
                    print("Case dejà modifiée")
        #on definit l'element du tableau ayant comme indice lig et col a symJouB
        tab[lig][col] = symJouB
        #on definit change a false
        change = False

        """Ligne et colonne"""
        #pour i chaque valeur de 0 a 3
        for i in range(0,3):
            #alors
            #si les elements d'une ligne ou d'une colonne sont egales a symJouB
            if tab[i][0]==symJouB and tab[i][1]==symJouB and tab[i][2]==symJouB or tab[0][i]==symJouB and tab[1][i]==symJouB and tab[2][i]==symJouB:
                #alors 
                # on appelle la fonction display
                for i in tab:
                    for j in i:
                        print(j, end="")
                    print()
                #on retourne les string vainqueur et nomJoueurB
                return vainqueur + nomJoueurB
          
    
        """diagonale"""
        #  si les elements des diagonales sont egales a symJouB
        if  tab[0][0]==symJouB and tab[1][1]==symJouB and tab[2][2]==symJouB or tab[2][0]==symJouB and tab[1][1]==symJouB and tab[0][2]==symJouB:
            #alors 
            # on appelle la fonction display
            for i in tab:
                for j in i:
                    print(j, end="")
                print()
            #on retourne les string vainqueur et nomJoueurB
            return vainqueur + nomJoueurB

        # on appelle la fonction display    
        for i in tab:
            for j in i:
                print(j, end="")
            print()
    
    

#on assigne a demande le string du retour de la fonction input
demande = input("Voulez-vous jouer au morpion ? \n")
while demande != "oui" :
    demande = input("Voulez-vous jouer au morpion ? \n")
#tant que demande est egal a "yes"
while demande == "oui":
    #alors
    #on affiche la fonction morpion
    print(morpion(1))
    #on assigne a demande le string du retour de la fonction input
    demande = input("Voulez-vous rejouer au morpion ? \n")
    while demande != "oui" :
        demande = input("Voulez-vous rejouer au morpion ? \n")