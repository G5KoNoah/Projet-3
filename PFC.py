import random
#on admet une fonction random qui retourne un chiffre aleatoire entre 0 et 2 compris
def random_nb():
    return random.randint(0,2)
#on admet une fonction input qui recupere l'entree d'un joueur

#on definit une fonction PFC avec comme parametre nombreJoueur et turnWin
def PFC(nombreJoueur,turnWin):
    #on determine un tableau avec comme valeur "pierre" , "feuille" et "ciseaux"
    tab = ["pierre","feuille","ciseaux"]
    #on determine noWin a true
    noWin=True
    #on initialise pointJoueurA a 0
    pointJoueurA = 0
    #on initialise pointJoueurB a 0
    pointJoueurB = 0
    #on affiche "nom du joueur 1: "
    print("Le nom du joueur 1 : ")
    #on assigne a nomJoueurA le string du retour de l'execution de la fonction input
    nomJoueurA = input()
    #si il n'y a qu'un joueur
    if nombreJoueur == 1 :
        #alors on determine nomJoueurB a "IA"
        nomJoueurB = "IA"
    #sinon
    else :
        #on affiche "nom du joueur 2: "
        print("Le nom du joueur 2 : ")
        #on assigne a nomJoueurB le string du retour de l'execution de la fonction input
        nomJoueurB = input()

    #tant que noWin est egal a true
    while noWin :
        #alors
        #on assigne a choixJoueurA le retour de l'execution de la fonction input
        choixJoueurA = int(input("choix du joueur 1 : \n pierre = 0 feuille = 1 ciseaux = 2 \n"))
        #on vérifie si la fonction input renvoie les bonnes valeurs
        while choixJoueurA != 0 and choixJoueurA !=1 and choixJoueurA !=2 :
            choixJoueurA = int(input("resaisir le choix du joueur 1 : \n pierre = 0 feuille = 1 ciseaux = 2 \n"))
        #si il n'y a qu'un joueur
        if nombreJoueur == 1 :
            #alors on assigne a choixJoueurB le retour de l'execution de la fonction random
            choixJoueurB = random_nb()
        #sinon on assigne a choixJoueurB le retour de l'execution de la fonction input
        else : 
            choixJoueurB = int(input("choix du joueur 2 :\n pierre = 0 feuille = 1 ciseaux = 2 \n"))

        #on affiche nomJoueurA et le tableau avec comme indice choixJoueurA
        print(nomJoueurA + " : " + tab[choixJoueurA])
        #on affiche nomJoueurB et le tableau avec comme indice choixJoueurB
        print(nomJoueurB + " : " + tab[choixJoueurB])
        #si choixJoueurA est égal a 0
        if choixJoueurA == 0 :
            #alors
            #si choixJoueurB est égal a 0
            if choixJoueurB == 0 :
                #alors 
                #on affiche "égalité"
                print("Egalité" +"\n")

            #si choixJoueurB est égal a 1
            if choixJoueurB == 1 :
                #alors 
                #on incremente poinJoueurB de 1
                pointJoueurB = pointJoueurB + 1
                #on affiche "le vainqueur de la manche est " et nomJoueurB
                print("Le vainqueur de la manche est : " + nomJoueurB + "\n")
        
            #si choixJoueurB est égal a 2
            if choixJoueurB == 2 :
                #alors 
                #on incremente poinJoueurA de 1
                pointJoueurA = pointJoueurA + 1
                #on affiche "le vainqueur de la manche est " et nomJoueurA
                print("Le vainqueur de la manche est : " + nomJoueurA + "\n")

        #sinon si choixJoueurA est égal a 1
        elif choixJoueurA == 1 :
            #alors
            #si choixJoueurB est égal a 1
            if choixJoueurB == 1 :
                #alors 
                #on affiche "égalité"
                print("Egalité" +"\n")

            #si choixJoueurB est égal a 2
            if choixJoueurB == 2 :
                #alors 
                #on incremente poinJoueurB de 1
                pointJoueurB = pointJoueurB + 1
                #on affiche "le vainqueur de la manche est " et nomJoueurB
                print("Le vainqueur de la manche est : " + nomJoueurB + "\n")
        
            #si choixJoueurB est égal a 0
            if choixJoueurB == 0 :
                #alors 
                #on incremente poinJoueurA de 1
                pointJoueurA = pointJoueurA + 1
                #on affiche "le vainqueur de la manche est " et nomJoueurA
                print("Le vainqueur de la manche est : " + nomJoueurA + "\n")
        
        #sinon
        else :
            #alors
            #si choixJoueurB est égal a 2
            if choixJoueurB == 2 :
                #alors 
                #on affiche "égalité"
                print("Egalité" +"\n")

            #si choixJoueurB est égal a 0
            if choixJoueurB == 0 :
                #alors 
                #on incremente poinJoueurB de 1
                pointJoueurB = pointJoueurB + 1
                #on affiche "le vainqueur de la manche est " et nomJoueurB
                print("Le vainqueur de la manche est : " + nomJoueurB +"\n")
        
            #si choixJoueurB est égal a 1
            if choixJoueurB == 1 :
                #alors 
                #on incremente poinJoueurA de 1
                pointJoueurA = pointJoueurA + 1
                #on affiche "le vainqueur de la manche est " et nomJoueurA
                print("Le vainqueur de la manche est : " + nomJoueurA+ "\n")
            

        #on affiche nomJoueurA et pointJoueurA
        print(nomJoueurA + " : " + str(pointJoueurA))
        #on affiche nomJoueurB et pointJoueurB
        print(nomJoueurB + " : " + str(pointJoueurB) + "\n")
        #si pointJoueurA est egal a turnWin
        if pointJoueurA == turnWin :
            #alors
            #on passe noWIn a false
            noWin = False
            #on determine vainqueur a nomJoueurA
            vainqueur = nomJoueurA
        #si pointJoueurB est egal a turnWin
        if pointJoueurB == turnWin :
            #alors
            #on passe noWIn a false
            noWin = False
            #on determine vainqueur a nomJoueurB
            vainqueur = nomJoueurB

    #on affiche "le vainqueur est : " et vainqueur
    print("Le vainqueur est : " + vainqueur)
    return "end"
#fin fonction

#on appelle la fonction
print(PFC(1,3))
