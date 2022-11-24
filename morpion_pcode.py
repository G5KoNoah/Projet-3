
#on definit une fonction input qui récupere l'entree d'un joueur

#on definit une fonction display qui renvoie un affichage d'une liste de liste en tableau

#on definit une fonction first avec comme parametre une liste et qui renvoie les indices de la premiere valeur du tableau qui est egal a " □ " 

#on definit une fonction checkWin avec comme parametre un symbole et un tableau 
    #elle verifie pour chaque colonne et chaque ligne du tableau que si il y a 3 parametre symbole elle renvoie le symbole
    #elle verifie pour chaque diagonale du tableau que si il y a 3 parametre symbole elle renvoie le symbole

#on definit une fonction checkIA avec comme parametre un symbole et un tableau
    #elle verifie que pour chaque ligne, colonne et diagonale que si deux parametres symboles sont presents et que si la troisieme case est vide alors elle renvoie la ligne et la colonne de la case vide

#on definit une fonction morpion avec comme parametre le nombreJoueur 
    #on initialise un tableau avec 3 listes qui contiennent 3 caracteres vides □
    #on initialise noWin a True
    #on initialise nbTour a 0
    #on definit vainqueur au string "Le vainqueur est : "
    
    #on initialise change a False
    #si il n'y a qu'un joueur
        #alors
        #on initialise start a un string vide
        #tant que start est different de "oui" et de "non"
            #alors on assigne start au retour de l'execution de la fonction input
        #si start est egal a "oui"
            #alors
            #on assigne nomJoueurA le string du retour de l'execution de la fonction input 
            #on determine nomJoueurB a "IA"
        #sinon
            #alors
            #on assigne nomJoueurB le string du retour de l'execution de la fonction input
            #on determine nomJoueurA a "IA"
        #on initialise config a un string vide
    #sinon
        #on assigne nomJoueurA le string du retour de l'execution de la fonction input 
        #on assigne a nomJoueurB le string du retour de l'execution de la fonction input

    #si start est egal a "non"
        #alors
        #on definit symboleJoueurA a un string vide
        #on assigne  symboleJoueurB le string du retour de la fonction input
        #tant que symboleJoueurB est different de "X" et "O" 
            #alors on reassigne  symboleJoueurB le string du retour de la fonction input
        #si symboleJoueurA est egal a "O"
            #alors
            #on initialise symJouA a " X "
            #on initialise symJouB a " O "
        #sinon
            #alors
            #on initialise symJouA a " O "
            #on initialise symJouB a " X "
            #on execute la fonction display
    #sinon
        #alors
        #on assigne  symboleJoueurA le string du retour de la fonction input
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
        #si nomJoueurA est egal a "IA"
            #alors
            #si nbTour est egal a 1
                #alors
                #on definit lig a 2
                #on definit col a 0
            #si nbTour est egal a 2
                #alors 
                #si la case du centre est prise par symJouB
                    #alors
                    #on definit lig a 0
                    #on definit col a 2
                #sinon
                    #alors
                    #si la case au centre a gauche est prise par symJouB
                        #alors
                        #on definit lig a 2
                        #on definit col a 2
                    #sinon si la case en haut a gauche est vide
                        #alors
                        #on definit config a "win"
                        #on definit lig a 0
                        #on definit col a 0
                    #sinon
                        #alors
                        #on definit lig a 2
                        #on definit col a 2
            #si nbTour est egal a 3
                #alors
                # si config est egal a "win" et que la case en bas a droite est vide
                    #alors
                    #on definit lig a 2
                    #on definit col a 2
                #sinon
                    #alors
                    #on definit lig a 0
                    #on definit col a 2

            #on definit c le retour de la fonction checkIA avec comme parametre symJouB et tab       
            #si checkIA retourne une valeur
                #alors
                #on definit lig a c avec l'indice 0
                #on definit col a c avec l'indice 1

            #on definit c le retour de la fonction checkIA avec comme parametre symJouA et tab       
            #si checkIA retourne une valeur
                #alors
                #on definit lig a c avec l'indice 0
                #on definit col a c avec l'indice 1             
        #sinon
            #alors
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

        #on appelle la fonction display
        #on definit c le retour de la fonction checkWin avec comme parametre symJouA et tab
        #si c est egal a symJouA
            #on retourne vainqueur plus nomJoueurA
        
        #si nbTour est egal a 5
            #on retourne "Egalite"

        #on affiche "Choix du joueur 2 :"

        #si nomJoueur est egal a "IA"
            #alors 
            #on definit r au retour de la fonction first
            #on definit lig a r d'indice 0
            #on definit col a r d'indice 1

            #si on est au premier tour donc que nbTour est egal a 1
                #alors
                #si le symbole du joueur 1 est place dans un coin
                    #alors
                    #on definit lig a 1
                    #on definit col a 1
                    #on definit config a "coin"
                #sinon si le symbole du joueur 1 est place au centre
                    #alors
                    #on definit lig a 0
                    #on definit col a 0
                #sinon   
                    #alors
                    #on definit lig a 1
                    #on definit col a 1
                    #on definit config a "coin"

            #si on est au deuxieme tour donc que nbTour est egal a 2
                #si config est "coin"
                    #si la case en haut a gauche est le symbole du joueur 1
                        #si la case en bas a droite est le symbole du joueur 1
                            #alors
                            #on definit lig a 2
                            #on definit col a 1
                        #si la case en bas au centre est le symbole du joueur 1
                            #alors
                            #on definit lig a 2
                            #on definit col a 0
                        #si la case au centre a droite est le symbole du joueur 1
                            #alors
                            #on definit lig a 0
                            #on definit col a 2
                    #sinon si le coin en haut a droite est le symbole du joueur 1
                        #si la case en bas a gauche est le symbole du joueur 1
                            #alors
                            #on definit lig a 2
                            #on definit col a 1
                        #si la case en bas au centre est le symbole du joueur 1
                            #alors
                            #on definit lig a 2
                            #on definit col a 2
                        #si la case au centre a gauche est le symbole du joueur 1
                            #alors
                            #on definit lig a 0
                            #on definit col a 0
                    #sinon si la case en bas a gauche est le symbole du joueur 1
                        #si la case en haut a droite est le symbole du joueur 1
                            #alors
                            #on definit lig a 0
                            #on definit col a 1
                        #si la case en haut au centre est le symbole du joueur 1
                            #alors
                            #on definit lig a 0
                            #on definit col a 0
                        #si la case au centre a droite est le symbole du joueur 1
                            #alors
                            #on definit lig a 2
                            #on definit col a 2
                    #sinon
                        #si la case en haut a gauche est le symbole du joueur 1
                            #alors
                            #on definit lig a 0
                            #on definit col a 1
                        #si la case an haut au centre est le symbole du joueur 1
                            #alors
                            #on definit lig a 0
                            #on definit col a 2
                        #si la case au centre a gauche est le symbole du joueur 1
                            #alors
                            #on definit lig a 2
                            #on definit col a 0
                #si config est egal a "bord"
                    #si la case en bas au centre est le symbole du joueur 1
                        #alors
                        #on definit lig a 2
                         #on definit col a 2
                    #si la case au centre a gauche est le symbole du joueur 1 et si la case au centre a droite est le symbole du joueur 1 ou si la case en haut au centre est le symbole du joueur 1 et si la case en bas au centre est le symbole du joueur 1
                        #alors
                        #on definit lig a 0
                        #on definit col a 0
            #si la case en haut au centre est le symbole du joueur 1 et si la case au centre a gauche est le symbole du joueur 1 et si la case en haut a gauche est vide
                #alors
                #on definit lig a 0
                #on definit col a 0
            #si la case en haut au centre est le symbole du joueur 1 et si la case au centre a droite est le symbole du joueur 1 et si la case en haut a gauche est vide
                #alors
                #on definit lig a 0
                #on definit col a 2
            #si la case au centre a droite est le symbole du joueur 1 et si la case en bas au centre est le symbole du joueur 1 et si la case en haut a gauche est vide
                #alors
                #on definit lig a 2
                #on definit col a 2
            #si la case en bas au centre est le symbole du joueur 1 et si la case au centre a gauche est le symbole du joueur 1 et si la case en haut a gauche est vide
                #alors
                #on definit lig a 2
                #on definit col a 0

            #on definit c le retour de la fonction checkIA avec comme parametre symJouA et tab       
            #si checkIA retourne une valeur
                #alors
                #on definit lig a c avec l'indice 0
                #on definit col a c avec l'indice 1

            #on definit c le retour de la fonction checkIA avec comme parametre symJouB et tab       
            #si checkIA retourne une valeur
                #alors
                #on definit lig a c avec l'indice 0
                #on definit col a c avec l'indice 1 
                        
        #sinon
            #alors
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
        #on definit l'element du tableau ayant comme indice lig et col a symJouB
        #on definit change a false
        #on appelle la fonction display
        #on definit c le retour de la fonction checkWin avec comme parametre symJouA et tab
        #si c est egal a symJouA
            #on retourne vainqueur plus nomJoueurA
    


#on assigne a demande le string du retour de la fonction input
#si demande est egal a "non"
    #alors on affiche "dommage"
#sinon
    #alors
    #tant que demande est different de "oui"
        #alors on assigne a demande le string du retour de la fonction input
    #on assigne a joueur le string du retour de la fonction input
    #tant que joueur est different de 1 et de 2
        #alors on assigne a joueur le string du retour de la fonction input
    #tant que demande est egal a "oui"
        #alors
        #on affiche la fonction morpion avec comme parametre joueur
        #on assigne a demande le string du retour de la fonction input
        #tant que demande est different de "oui"
            #alors on assigne a demande le string du retour de la fonction input
        #on assigne a joueur le string du retour de la fonction input
