from heapq import heappush, heappop
from sys import stdin

__author__ = 'Stian'

def main():
    lines = stdin.readlines()
    n = len(lines)
    adj_l = [{} for x in xrange(n)]
    for i in xrange(n):
        line = lines[i].split()
        line.reverse()
        for pair in line:
            adj, edge = pair.split(':')
            adj = int(adj)
            if adj <= i:
                break
            edge = int(edge)
            adj_l[i][adj] = edge
            adj_l[adj][i] = edge
            print(adj_l)
    max_w = 0
    not_visited = [1] * n
    not_visited[0] = 0
    edges = []
    [heappush(edges, (adj_l[0][i], i)) for i in adj_l[0]]
    for x in xrange(1, n):
        w, i = heappop(edges)
        while not not_visited[i]:
            w, i = heappop(edges)
        not_visited[i] = 0
        [heappush(edges, (adj_l[i][j], j)) for j in adj_l[i] if not_visited[j]]
        max_w = max(max_w, w)
    print max_w


main()
