import random
randomlist = []
d = 500000
for i in range(d):
    randomlist.append(random.randint(0, d))

def ordena(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]




ordena(randomlist)

