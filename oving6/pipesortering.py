from bisect import bisect
from sys import stdin
__author__ = 'Stian'

def rsort(A):
    ml = 1000000
    bckt = [[] for _ in range(0, 10)]
    for d in range(0, ml):
        for n in A:
            bckt[n / 10**d % 10].append(n)
        del A[:]
        for bucket in bckt:
            A.extend(bucket)
            del bucket[:]
    return A

def find(A, bot, top):
    i = bisect(A, bot)
    if top not in A:
        j = bisect(A, top)
        top = A[j - 1 if j >= len(A) else j]
    print str(A[i if i <= 0 else i - 1]), str(top)

def main():
    A = rsort(map(int, set(stdin.readline().split())))
    for line in stdin:
        arg = line.split()
        find(A, int(arg[0]), int(arg[1]))

main()