with open("e.txt", "r") as file:
    lines = [int(line.rstrip()) for line in file]


def wypisanie():
    print("elementy z tym jaka dlugosc listy itd", lines)
    wartosc = [lines[0]]
    rozmiar = [lines[1]]
    lista = [lines[i] for i in range(2, len(lines))]
    print("Tylko elementy listy", lista)


def oblicz():
    operacje = 0
    k = []

    wartosc = [lines[1]]
    index = lines[1]
    lista = [lines[i] for i in range(2, len(lines))]

    def quicksort(array, low, high):
        nonlocal operacje
        if low < high:
            pivot = partition(array, low, high)
            quicksort(array, low, pivot)
            quicksort(array, pivot + 1, high)

    def partition(array, low, high):
        nonlocal operacje
        pivot = array[(high + low) // 2]
        i = low
        j = high

        while True:
            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            operacje += 1
            array[i], array[j] = array[j], array[i]
            k.append(i)  # Dodaj zmianę indeksu do listy

    def sort(array, low, high):
        quicksort(array, low, high)
        return array

    sorted_array = sort(lista, 0, len(lista) - 1)
    print(f"Ilość elementów na liście: {wartosc[0]}")
    print(sorted_array)
    print(f"Liczba zmian indeksu: {len(k)}")

    with open("out1.txt", 'w') as f:
        f.write(str(sorted_array[index-1]))


def test():
    operacje = 0
    k = []
    wartosc = [lines[1]]
    index = lines[0]

    lista = [lines[i] for i in range(2, len(lines))]

    def quicksort(array, low, high):
        nonlocal operacje
        if low < high:
            pivot = partition(array, low, high)
            quicksort(array, low, pivot)
            quicksort(array, pivot + 1, high)

    def partition(array, low, high):
        nonlocal operacje
        pivot = array[(high + low) // 2]
        i = low
        j = high

        while True:

            while array[i] < pivot:
                i += 1
            while array[j] > pivot:
                j -= 1
            if i >= j:
                return j
            operacje += 1
            array[i], array[j] = array[j], array[i]

    def sort(array, low, high):
        quicksort(array, low, high)
        return array

    sorted_array = sort(lista, 0, len(lista) - 1)
    print(f"Ilosc elementow na liscie {wartosc[0]}")
    print(sorted_array)

    with open("out1.txt", 'w') as f:
        f.write(str(sorted_array[index-1]))


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
