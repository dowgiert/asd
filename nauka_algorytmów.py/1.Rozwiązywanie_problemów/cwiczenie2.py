#moje
from random import randint
def na_głupa_mediana():
    lista = [randint(0, 11) for i in range(100)]
    lista.sort()
    print(lista)
    if len(lista)%2==0:
        return (lista[int(len(lista)/2)]+lista[(int(len(lista)/2))-1])/2
    else:
        return lista[int(len(lista)/2)]

print(na_głupa_mediana())