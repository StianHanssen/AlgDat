__author__ = 'Stian'

from sys import stdin, stderr
import traceback


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def b(d):
    t = Node()
    for w, p in d:
        s = t
        for letter in w:
            if letter not in s.barn:
                s.barn[letter] = Node()
            s = s.barn[letter]
        s.posi.append(p)
    return t

def po(w, i, n):
    if i >= len(w):
        p = n.posi
    elif w[i] == "?":
        p = []
        for barn in n.barn.values():
            p += po(w, i + 1, barn)
    elif w[i] in n.barn:
        p = po(w, i + 1, n.barn[w[i]])
    else:
        p = []
    return p

def main():
    try:
        o = raw_input().split()
        l = []
        d = 0
        for c in o:
            l.append((c, d))
            d += len(c) + 1
        t = b(l)
        for s in stdin:
            s = s.strip()
            print s + ":",
            pos = po(s, 0, t)
            pos.sort()
            for p in pos:
                print p,
            print
    except:
        traceback.print_exc(file=stderr)

main()