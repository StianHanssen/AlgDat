__author__ = 'Stian'

from sys import *

def subgraftetthet(nabomatrise, startnode, n):
    i = 0
    nodes = [startnode]
    while i < len(nodes):
            line = nabomatrise[nodes[i]]
            nodes += [j for j in xrange(len(line)) if line[j] and j not in nodes]
            i += 1
    not_nodes = [j for j in xrange(n) if j not in nodes]
    kanter = sum(nabomatrise[j][k] for j in not_nodes for k in not_nodes)
    if len(not_nodes) == 0:
        return 0.0
    else:
        return float(kanter) / float(len(not_nodes)**2)
def main():
    n = int(stdin.readline())
    nabomatrise = [map(int, stdin.readline().strip()) for i in xrange(0, n)]
    for linje in stdin:
        start = int(linje)
        print "%.3f" % (subgraftetthet(nabomatrise, start, n) + 1E-12)

main()