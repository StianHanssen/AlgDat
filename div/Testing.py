__author__ = 'Stian'

def sorter(A):
    if len(A) <= 1:
        return A
    return sorter([x for x in A[1:] if x < A[0]]) + [A[0]] + sorter([x for x in A[1:] if x >= A[0]])

A = [9, 1, 53, 3, 5, 35, 5, 3, 44]
print(sorter(A))
