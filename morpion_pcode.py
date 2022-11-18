
#on definit une fonction input qui récupere l'entree d'un joueur

#on definit une fonction display qui renvoie un affichage d'une liste de liste en tableau

#on definit une fonction first avec comme parametre une liste et qui renvoie les indices de la premiere valeur du tableau qui est egal a " □ " 

#on definit une fonction morpion avec comme parametre le nombreJoueur 
    #on initialise un tableau avec 3 listes qui contiennent 3 caracteres vides □
    #on initialise noWin a True
    #on initialise nbTour a 0
    #on definit vainqueur au string "Le vainqueur est : "
    #on assigne nomJoueurA le string du retour de la fonction input 
    #on initialise change a False
    #si il n'y a qu'un joueur
        #alors on determine nomJoueurB a "IA"
    #sinon
        #on assigne a nomJoueurB le string du retour de l'execution de la fonction input

    #on assigne symboleJoueurA le string du retour de la fonction input 

    #tant que symboleJoueurA est different de "X" et "O" 
        #alors on reassigne  symboleJoueurA le string du retour de la fonction input 

    #si symboleJoueurA est egal a "X"
        #alors
        #on initialise symJouA a " X "
        #on initialise symJouB a " O "
    #sinon
        #alors
        #on initialise symJouA a " O "
        #on initialise symJouB a " X "
        
    #on execute la fonction display

    #tant que noWIn est vrai  
        #on incremente nbTour de 1
        #on affiche le string "Choix du joueur 1 :"
        #tant que change est faux
            #alors 
            #on assigne ligne le string du retour de la fonction input
            #tant que ligne est different de 1, de 2 et de 3
                #alors on assigne ligne au string du retour de la fonction input

            #on assigne colonne le string du retour de la fonction input
            #tant que colonne est different de 1, de 2 et de 3
                #alors on assigne colonne au string du retour de la fonction input
            #on definit lig a l'entier de ligne en retirant 1
            #on definit col a l'entier de colonne en retirant 1
            #si l'element du tableau ayant comme indice lig et col est egal a □ 
                #alors on definit change a vrai
            #sinon
                #alors on affiche "Case deja modifiee"
        #on definit l'element du tableau ayant comme indice lig et col a symJouA
        #on definit change a false

        """ligne et colonne"""
        #pour i chaque valeur de 0 a 3
            #alors
            #si les elements d'une ligne i ou d'une colonne i sont egales a symJouA 
                #alors 
                # on appelle la fonction display
                #on retourne les string vainqueur et nomJoueurA
           
        """diagonale"""
        #  si les elements des diagonales sont egales a symJouA 
            #alors 
            # on appelle la fonction display
            #on retourne les string vainqueur et nomJoueurA

        #on appelle la fonction display
        
        #si nbTour est egal a 5
            #on retourne "Egalite"

        #on affiche "Choix du joueur 2 :"

        #si nomJoueur est egal a "IA"
        if nomJoueurB=="IA" :
            #alors 
            #on definit r au retour de la fonction first
            r=first(tab)
            #on definit lig a r d'indice 0
            lig=r[0]
            #on definit col a r d'indice 1
            col=r[1]

            #si on est au premier tour donc que nbTour est egal a 1
            if nbTour==1:
                #alors
                #si le symbole du joueur 1 est place dans un coin
                if tab[0][0]==symJouA or tab[0][2]==symJouA or tab[2][0]==symJouA or tab[2][2]==symJouA :
                    #alors
                    #on definit lig a 1
                    lig=1
                    #on definit col a 1
                    col=1
                    #on definit config a "coin"
                    config="coin"
                #sinon si le symbole du joueur 1 est place au centre
                elif tab[1][1]==symJouA:
                    #alors
                    #on definit lig a 0
                    lig=0
                    #on definit col a 0
                    col=0
                #sinon   
                else :
                    #alors
                    #on definit lig a 1
                    #on definit col a 1
                    lig=1
                    col=1
                    #on definit config a "coin"
                    config="bord"

            #si on est au deuxieme tour donc que nbTour est egal a 2
            if nbTour==2:
                #si config est "coin"
                if config=="coin":
                    #si le coin en haut a gauche est le symbole du joueur 1
                    if tab[0][0]==symJouA   :
                        #si le coin en bas a droite est le symbole du joueur 1
                        if tab[2][2]==symJouA:
                            lig =2
                            col=1
                        #si le coin en bas au centre est le symbole du joueur 1
                        if tab[2][1]==symJouA :
                            lig=2
                            col=0
                        #si le coin au centre a droite est le symbole du joueur 1
                        if tab[1][2]==symJouA :
                            lig=0
                            col=2
                    #sinon si le coin en haut a droite est le symbole du joueur 1
                    elif tab[0][2]==symJouA :
                        #si le coin en bas a gauche est le symbole du joueur 1
                        if tab[2][0]==symJouA:
                            lig =2
                            col=1
                        #si le coin en bas au centre est le symbole du joueur 1
                        if tab[2][1]==symJouA :
                            lig=2
                            col=2
                        #si le coin au centre a gauche est le symbole du joueur 1
                        if tab[1][0]==symJouA :
                            lig=0
                            col=0
                    #sinon si le coin en bas a gauche est le symbole du joueur 1
                    elif tab[2][0]==symJouA :
                        #si le coin en haut a droite est le symbole du joueur 1
                        if tab[0][2]==symJouA:
                            lig =0
                            col=1
                        #si le coin en haut au centre est le symbole du joueur 1
                        if tab[0][1]==symJouA :
                            lig=0
                            col=0
                        #si le coin au centre a droite est le symbole du joueur 1
                        if tab[1][2]==symJouA :
                            lig=2
                            col=2
                    #sinon
                    else:
                        if tab[0][0]==symJouA:
                            lig =0
                            col=1
                        if tab[0][1]==symJouA :
                            lig=0
                            col=2
                        if tab[1][0]==symJouA :
                            lig=2
                            col=0
                if config=="bord":
                    if tab[2][1]==symJouA and tab[0][2]==symJouA:
                        lig=2
                        col=2
                    if tab[1][0]== symJouA and tab[1][2]==symJouA or tab[0][1]== symJouA and tab[2][1]==symJouA:
                        lig=0
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
                expli(tab)
                #on retourne les string vainqueur et nomJoueurB
                return vainqueur + nomJoueurB
          
    
        """diagonale"""
        #  si les elements des diagonales sont egales a symJouB
        if  tab[0][0]==symJouB and tab[1][1]==symJouB and tab[2][2]==symJouB or tab[2][0]==symJouB and tab[1][1]==symJouB and tab[0][2]==symJouB:
            #alors 
            # on appelle la fonction display
            expli(tab)
            #on retourne les string vainqueur et nomJoueurB
            return vainqueur + nomJoueurB

        # on appelle la fonction display    
        expli(tab)
    


#on assigne a demande le string du retour de la fonction input
demande = input("Voulez-vous jouer au morpion ? \n")
if demande=="non":
    print("Dommage :(")
else:
    while demande != "oui" :
        demande = input("Voulez-vous jouer au morpion ? \n")
    #tant que demande est egal a "yes"
    joueur=int(input("Combien y a t-il de joueur ? \n"))
    while joueur !=1 and joueur !=2:
        joueur=int(input("Il ne peut y avoir qu'un ou deux joueurs \n"))
    while demande == "oui":
        #alors
        #on affiche la fonction morpion
        print(morpion(joueur))
        #on assigne a demande le string du retour de la fonction input
        demande = input("Voulez-vous rejouer au morpion ? \n")
        while demande != "oui" :
            demande = input("Voulez-vous rejouer au morpion ? \n")
        joueur=int(input("Combien y a t-il de joueur ? \n"))
