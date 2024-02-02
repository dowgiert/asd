A = [5, 2, 6, 7, 5, 8, 9, 5]
B = [3, 2]
def largest_samemu(A):
    if len(A)<2:
        print("Nie wystarczająca długość.")
    else:
        lista = [A[0], A[1]]
        for i in range(2, len(A)):
            if lista[0]>lista[1]:
                lista[0],lista[1]=lista[1],lista[0]
            if A[i]>lista[0]:
                lista[0] = A[i]
    return lista            

print(largest_samemu(A))

def largest_two(A):
    my_max, second = A[:2]
    if my_max <second:
        my_max, second = second, my_max
    
    for idx in range(2, len(A)):
        if my_max < A[idx]:
            my_max, second = A[idx], my_max
        elif second < A[idx]:
            second = A[idx]
    return (my_max, second)

b = largest_two(A)
print(b)