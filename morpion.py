
def morpion(nombreJoueur):
    vainqueur = "Le vainqueur est : "
    tab = [[" □ " for i in range(3)] for j in range(3)]
    noWin = True
    nbTour = 0
    nomJoueurA = input("Le nom du joueur 1 : \n")
    change = False

    if nombreJoueur == 1 :
        nomJoueurB = "IA"
        config=""
    else :
        nomJoueurB = input("Le nom du joueur 2 : \n")

    symboleJoueurA = input("Symbole du joueur 1 : \n X ou O \n")

    while symboleJoueurA != "X" and symboleJoueurA != "O" :
        symboleJoueurA = input("Veuillez resaisir le symbole du joueur 1 : \n")

    if symboleJoueurA == "X" :
        symJouA = " X "
        symJouB = " O "
    else :
        symJouA = " O "
        symJouB = " X "
        
    expli(tab)

    while noWin:
        nbTour = nbTour + 1 
        print("Choix du joueur 1 : \n")
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

        c=checkWin(symJouA,tab)
        expli(tab)
        if c==symJouA:
            return vainqueur + nomJoueurA

        
        if nbTour == 5 :
            return "Egalite"

        print("Choix du joueur 2 : \n")

        if nomJoueurB=="IA" :
            
            r=first(tab)
            lig=r[0]
            col=r[1]

            if nbTour==1:
                if tab[0][0]==symJouA or tab[0][2]==symJouA or tab[2][0]==symJouA or tab[2][2]==symJouA :
                    lig=1
                    col=1
                    config="coin"
                elif tab[1][1]==symJouA:
                    lig=0
                    col=0
                else:
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
                               
            c=checkIA(symJouA,tab)
            if c !=None:
                lig=c[0]
                col=c[1]

            c=checkIA(symJouB,tab)
            if c!=None:
                lig=c[0]
                col=c[1]

        else :
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
        tab[lig][col] = symJouB
        change = False
        expli(tab)
        c=checkWin(symJouB,tab)
        if c==symJouB:
            return vainqueur + nomJoueurB

def expli(tab):
    c=[1,2,3]
    print(" 1  2  3")
    t=0
    for i in tab:
        for j in i:
            print(j, end="")
        print( c[t])
        t=t+1

def checkWin(symJoueur,tab):
    """ligne et colonne"""
    for i in range(0,3):
        if tab[i][0]==symJoueur and tab[i][1]==symJoueur and tab[i][2]==symJoueur or tab[0][i]==symJoueur and tab[1][i]==symJoueur and tab[2][i]==symJoueur :
            return symJoueur
    """diagonale"""
    if tab[0][0]==symJoueur and tab[1][1]==symJoueur and tab[2][2]==symJoueur or tab[2][0]==symJoueur and tab[1][1]==symJoueur and tab[0][2]==symJoueur :
        return symJoueur

def first(tab):
    for i in range(0,3):
        for j in range(0,3) :
            if tab[i][j]== " □ ":
                return i,j    

def checkIA(symJoueur,tab):
    for i in range(0,3):
        if tab[i][0]==symJoueur and tab[i][1]==symJoueur and tab[i][2]==" □ ":
            lig=i
            col=2
            return lig,col
        if tab[i][0]==symJoueur and tab[i][2]==symJoueur and tab[i][1]==" □ ":
            lig=i
            col=1
            return lig,col
        if tab[i][1]==symJoueur and tab[i][2]==symJoueur and tab[i][0]==" □ ":
            lig=i
            col=0
            return lig,col
        if tab[0][i]==symJoueur and tab[1][i]==symJoueur and tab[2][i]==" □ ":
            lig=2
            col=i
            return lig,col
        if tab[0][i]==symJoueur and tab[2][i]==symJoueur and tab[1][i]==" □ ":
            lig=1
            col=i
            return lig,col
        if tab[1][i]==symJoueur and tab[2][i]==symJoueur and tab[0][i]==" □ ":
            lig=0
            col=i
            return lig,col

    if tab[0][0]==symJoueur and tab[1][1]==symJoueur and tab[2][2]==" □ ":
        lig=2
        col=2
        return lig,col 
    if tab[0][0]==symJoueur and tab[2][2]==symJoueur and tab[1][1]==" □ ":
        lig=1
        col=1
        return lig,col 
    if tab[2][2]==symJoueur and tab[1][1]==symJoueur and tab[0][0]==" □ ":
        lig=0
        col=0
        return lig,col
    if tab[0][2]==symJoueur and tab[1][1]==symJoueur and tab[2][0]==" □ ":
        lig=2
        col=0
        return lig,col
    if tab[0][2]==symJoueur and tab[2][0]==symJoueur and tab[1][1]==" □ ":
        lig=1
        col=1
        return lig,col
    if tab[1][1]==symJoueur and tab[2][0]==symJoueur and tab[0][2]==" □ ":
        lig=0
        col=2
        return lig,col
    
demande = input("Voulez-vous jouer au morpion ? \n")
if demande=="non":
    print("Dommage :(")
else:
    while demande != "oui" :
        demande = input("Voulez-vous jouer au morpion ? \n")
    joueur=int(input("Combien y a t-il de joueur ? \n"))
    while joueur !=1 and joueur !=2:
        joueur=int(input("Il ne peut y avoir qu'un ou deux joueurs \n"))
    while demande == "oui":
        print(morpion(joueur))
        demande = input("Voulez-vous rejouer au morpion ? \n")
        while demande != "oui" :
            demande = input("Voulez-vous rejouer au morpion ? \n")
        joueur=int(input("Combien y a t-il de joueur ? \n"))
