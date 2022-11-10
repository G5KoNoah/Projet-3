
def tableau(x,y,t):
    tab = [[0 for j in range(t)] for i in range(t)]
    tab[x-1][y] = 1
    tab[x][y] = 1
    tab[t-(t-x-1)][y] = 1
    tab[x][y-1] = 1
    tab[x][t-(t-y-1)] = 1
    for i in range(len(tab)):
        print(tab[i])


print(tableau(0,1,3))

t=[5,10,7,9,7,8]
print(t[4-2])