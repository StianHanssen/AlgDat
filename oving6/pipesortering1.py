from bisect import bisect
from sys import stdin
__author__ = 'Stian'

def msort(A):
    m = len(A)//2
    l, r = A[:m], A[m:]
    if len(l) > 1:
        l = msort(l)
    if len(r) > 1:
        r = msort(r)
    re = []
    while l and r:
        if l[-1] >= r[-1]:
            re.append(l.pop())
        else:
            re.append(r.pop())
    re.reverse()
    return (l or r) + re

def find(A, bot, top):
    i = bisect(A, bot)
    if top not in A:
        j = bisect(A, top)
        top = A[j - 1 if j >= len(A) else j]
    print str(A[i if i <= 0 else i - 1]), str(top)

def main():
    A = msort(map(int, stdin.readline().split()))
    for line in stdin:
        arg = line.split()
        find(A, int(arg[0]), int(arg[1]))

main()