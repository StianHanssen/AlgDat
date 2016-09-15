from sys import stdin
from itertools import repeat

def partition(seq):
    pi, seq = seq[0], seq[1:]
    lo = [x for x in seq if x <= pi]
    hi = [x for x in seq if x > pi]
    return lo, pi, hi

def qsort(seq):
    if len(seq) <= 1: 
        return seq
    lo, pi, hi = partition(seq)
    return qsort(lo) + [pi] + qsort(hi)

def merge(decks):
    return "".join([str(e[1]) for e in decks])

decks = []
for line in stdin:
    (index, seq) = line.split(':')
    decks += zip(map(int, seq.split(',')), repeat(index))
print merge(qsort(decks))