def palindrome(A):
    if A[::-1] == A:
        return True

def advanced_palindrome(A):
    A = A.lower()
    A = A.replace(" ", "")
    if A == A[::-1]:
        return True

print(advanced_palindrome("Marzena pokazała Zakopane z ram"))

