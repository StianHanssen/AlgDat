from sys import stdin
from itertools import repeat

def main():
    decks = []
    for line in stdin:
        (index, list) = line.split(':')
        decks += zip(map(int, list.split(',')), repeat(index))
    pos = [""] * (len(decks) + 100)
    for e in decks:
        pos[e[0] + 99] = str(e[1])
    print "".join(pos)

main()