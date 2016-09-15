import sys

INF = sys.maxint
NIL = "NIL"

def matrix_to_dict(nm):
    w = {}
    n = len(nm)
    for i in xrange(1, n + 1):
        for j in xrange(1, n + 1):
            w[i, j] = nm[i - 1][j - 1]
    return w, n

def dict_to_matrix(w, n):
    nm = [[0 for i in xrange(n)] for j in xrange(n)]
    for i in xrange(1, n + 1):
        for j in xrange(1, n + 1):
            if w[i, j] == INF:
                nm[i - 1][j - 1] = "~".rjust(2)
            else:
                nm[i - 1][j - 1] = str(w[i, j]).rjust(2)
    for i in xrange(len(nm)):
        print nm[i]
        
def floyd_warshall(w, p, n, u):
    d = {0: w}
    pi = {0: p}
    for k in range(1, n + 1):
        d[k] = {}
        pi[k] = {}
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if d[k - 1][i, j] > d[k - 1][i, k] + d[k - 1][k, j]:
                    d[k][i, j] = d[k - 1][i, k] + d[k - 1][k, j]
                    pi[k][i, j] = k
                else:
                    d[k][i, j] = d[k - 1][i, j]
                    pi[k][i,j] = pi[k - 1][i, j]
    return d[u], pi[u]

def main():  
    nm = [[0, INF, 5, INF, INF],
          [1, 0, INF, INF, 4],
          [INF, 9, 0, -1, INF],
          [4, 6, INF, 0, INF],
          [INF, INF, INF, -8, 0]]
    pi = [[NIL, NIL, 1, NIL, NIL], 
          [2, NIL, NIL, NIL, 2], 
          [NIL, 3, NIL, 3, NIL], 
          [4, 4, NIL, NIL, NIL], 
          [NIL, NIL, NIL, 5, NIL]]
    graph, n = matrix_to_dict(nm)
    pi, _ = matrix_to_dict(pi)
    graph_k, pi_k = floyd_warshall(graph, pi, n, 5)
    dict_to_matrix(pi_k, n)
    dict_to_matrix(graph_k, n)

main()

