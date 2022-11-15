#on definit une fonction input qui récupere l'entree d'un joueur


#on definit une fonction morpion
def morpion():
    #on initialise un tableau avec 3 listes qui contiennent 3 caracteres vides  
    tab = [[" ࠀ " for i in range(3)] for j in range(3)]
    noWin = True
    vainqueur = "Le vainqueur est : "
    for i in tab:
        for j in i:
            print(j, end="")
        print()
    while noWin:
        print("choixJoueur 1 : \n")
        ligne = int(input("ligne : \n"))
        while ligne !=1 and ligne !=2 and ligne !=3 :
            ligne = int(input("\n Veuillez resaisir la ligne : \n"))
        #on initialise colonne avec l'appelle de la fonction input
        colonne = int(input("Colonne : \n"))
        while colonne !=1 and colonne !=2 and colonne !=3 :
            ligne = int(input("\n Veuillez resaisir la colonne : \n"))
        #on affiche tab avec la fonction display
        lig = ligne-1
        col = colonne-1
        tab[lig][col] = " X "

        #ligne
        for i in range(0,3):
            if tab[i][0]==" X " and tab[i][1]==" X " and tab[i][2]==" X " :
                noWin = False
                return vainqueur + " X "
        
        
        #colonne
        for i in range(0,3):
            if tab[0][i]==" X " and tab[1][i]==" X " and tab[2][i]==" X " :
                noWin = False
                return vainqueur + " X "


        
        #diagonale
        if tab[0][0]==" X " and tab[1][1]==" X " and tab[2][2]==" X " :
            noWin = False
            return vainqueur + " X "

        if tab[2][0]==" X " and tab[1][1]==" X " and tab[0][2]==" X ":
            noWin = False
            return vainqueur + " X "

        for i in tab:
            for j in i:
                print(j, end="")
            print()

        print("choixJoueur 2 : \n")
        ligne = int(input("ligne : \n"))
        #on initialise colonne avec l'appelle de la fonction input
        colonne = int(input("Colonne : \n"))
        #on affiche tab avec la fonction display
        lig = ligne-1
        col = colonne-1
        tab[lig][col] = " O "

        #ligne
        for i in range(0,3):
            if tab[i][0]==" O " and tab[i][1]==" O " and tab[i][2]==" O " :
                noWin = False
                return vainqueur + " O "
        
        
        #colonne
        for i in range(0,3):
            if tab[0][i]==" O " and tab[1][i]==" O " and tab[2][i]==" O " :
                noWin = False
                return vainqueur + " O "        
        #diagonale
        if  tab[0][0]==" O " and tab[1][1]==" O " and tab[2][2]==" O ":
            noWin = False
            return vainqueur + " O "

        if tab[2][0]==" O " and tab[1][1]==" O " and tab[0][2]==" O ":
            noWin = False
            return vainqueur + " O "
            
        for i in tab:
            for j in i:
                print(j, end="")
            print()

demande = input("Voulez-vous jouer au morpion ? Yes or No \n")
while demande == "Yes":
    print(morpion())
    demande = input("Voulez-vous rejouer au morpion ? Yes or No \n")