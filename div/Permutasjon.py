def test(A, n):
    m = len(A)
    while m < n:
        s = list(A[0])
        i = ((m + 2) % 3) + 1
        temp = s[0]
        s[0] = s[i]
        s[i] = temp
        print s
        A.insert(0, s)
        m += 1
    return A

seq = [[1, 2, 3, 4]]
n = 24
l = [tuple(x) for x in test(seq, n)]
l.sort()
print l
print len(l)
