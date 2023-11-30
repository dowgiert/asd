# 1- sortowanie robić przez scalanie lub szybkie(quicksort)
# 2- algorytm horeas

with open("e.txt", "r") as file:
    lines = [int(line.rstrip()) for line in file]


def wypisanie():
    print("elementy z tym jaka dlugosc listy itd", lines)
    wartosc = [lines[0]]
    rozmiar = [lines[1]]
    lista = [lines[i] for i in range(2, len(lines))]
    print("Tylko elementy listy", lista)


def oblicz():
    wartosc = [lines[0]]
    lista = [lines[i] for i in range(2, len(lines))]

    def quickSort(L, left, right):
        operations = 0
        if left < right:
            q, ops = partition(L, left, right)
            operations += ops
            operations += quickSort(L, left, q-1)
            operations += quickSort(L, q+1, right)
        return operations

    def partition(L, left, right):
        pivot = L[left]
        i = left+1
        j = right
        operations = 0

        while True:
            while i <= j and L[i] <= pivot:
                i = i+1
                operations += 1
            while L[j] >= pivot and j >= i:
                j = j-1
                operations += 1
            if j < i:
                break
            else:
                L[i], L[j] = L[j], L[i]

        L[left], L[j] = L[j], L[left]
        return j, operations

    total_operations = quickSort(lista, 0, len(lista)-1)
    print(f"{wartosc[0]}-tym elementem na liście jest {lista[wartosc[0]-1]}")

    with open("out1.txt", 'w') as f:
        f.write(str(lista[wartosc[0]-1]) + '\n')

    print(f"Liczba wykonanych operacji {total_operations}")


def test():
    operacje = 0
    k = []
    wartosc = [lines[0]]
    rozmiar = [lines[1]]
    print("Ilość danych: ", lines[1])
    lista = [lines[i] for i in range(2, len(lines))]

    def quickSort(L, left, right):
        nonlocal operacje
        if left < right:
            q = partition(L, left, right)
            quickSort(L, left, q-1)
            quickSort(L, q+1, right)
        return L

    def partition(L, left, right):
        pivot = L[left]
        i = left+1
        j = right
        done = False
        while not done:
            while i <= j and L[i] <= pivot:
                i = i+1  # zwieksza az znajdzie pivot
                k.append(i)
            while L[j] >= pivot and i <= j:
                j = j-1  # zmniejsza az znajdzie pivot
                k.append(i)
            if j < i:
                done = True
            else:
                temp = L[i]
                L[i] = L[j]
                L[j] = temp
        temp = L[left]
        L[left] = L[j]
        # zamiana
        L[j] = temp
        return j

    save = [lista[wartosc[0]-1]]
    score = [save[0]]
    print(quickSort(lista, 0, len(lista)-1))

    with open("out1.txt", 'w') as f:
        for s in score:
            f.write(str(lista[wartosc[0]-1]))


while True:
    x = int(input("1.Dane, 2.Oblicz, 3.Test, 4. Koniec: "))
    if x == 1:
        wypisanie()
    elif x == 2:
        oblicz()

    elif x == 3:
        test()

    elif x == 4:
        break
