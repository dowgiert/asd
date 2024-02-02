A = [5, 3, 7, 6, 8, 2, 1, 9]
def tournament_two(A):
    winner = [None]*(len(A)-1)
    loser = [None]*(len(A)-1)
    prior = [-1]*(len(A)-1)
    idx = 0
    for i in range(0, len(A), 2):
        if A[i] < A[i+1]:
            winner[idx] = A[i+1]
            loser[idx] = A[i]
        elif A[i]>A[i+1]:
            winner[idx] = A[i]
            loser[idx] = A[i+1]
        idx += 1
    
    m=0
    while idx < len(A)-1:
        if winner[m]<winner[m+1]:
            winner[idx] = winner[m+1]
            loser[idx] = winner[m]
            prior[idx] = m+1
        else:
                winner[idx] = winner[m]
                loser[idx] = winner[m+1]
                prior[idx] = m

        idx += 1
        m += 2

#to jeszcze przemyśleć, bo nie do końca kumam xdd
    largest = winner[m]
    second = loser[m]
    m = prior[m]
    while m>=0:
        if second < loser[m]:
            second = loser[m]
        m = prior[m]
    return (largest, second)
wynik = tournament_two(A)
print(wynik)