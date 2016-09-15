def Solver(A, B):
    if not A:
        return True
    for i in xrange(len(A)):
        if sum(A[:i + 1]) in B and Solver(A[i + 1:], B):
            print "Found"
            return True
    return False

A = [2, 4, 5, 1, 2, 2, 9, -5]
B = [6, 8]

print Solver(A, B)