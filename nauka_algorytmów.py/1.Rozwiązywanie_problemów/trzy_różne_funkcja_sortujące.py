A = [5, 2, 6, 7, 5, 8, 9, 5]

def sorting_two(A):
    return tuple(sorted(A, reverse=True)[:2])

#print(tuple(A[0:3])) #fajna składnia
print(sorting_two(A))

def double_two(A):
    my_max = max(A)
    copy = list(A)
    copy.remove(my_max)
    return my_max, max(copy)

print(double_two(A))

def mutable_two(A):
    idx= max(range(len(A)), key=A.__getitem__)
    my_max = A[idx]
    del A[idx]
    second = max(A)
    A.insert(idx, my_max)
    return (my_max, second)

print(mutable_two(A))