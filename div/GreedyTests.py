def Looroo(S, F, k, n):
    m = k + 1
    while m <= n and S[m - 1] < F[k - 1]:
        m += 1
    if m <= n:
        return [m] + Looroo(S, F, m, n)
    return []

def Nuguzz(S, F):
    n = len(S)
    A = [0]
    j = 0
    for i in xrange(1, n):
        if F[i] >= S[j]:
            A += [i]
            j = i
    return A

def Zodit(S, F):
    n = len(S)
    A = [1]
    j = 1
    for i in xrange(2, n):
        if F[i] <= S[j]:
            A += [i]
            j = i
    return A

S = [3,5,3,2]
F = [9,7,4,3]
print Nuguzz(S, F)
