from sys import stdin
from _ast import Num

def heappop(Q):
    Q[0], Q[-1] = Q[-1], Q[0]
    val = Q.pop()
    n = len(Q)
    i = 0
    while True:
        left = 2 * i + 1
        right = left + 1
        if left < n:
            pos = left
            if right < n and Q[right][0] > Q[left][0]:
                pos = right
            if Q[pos][0] > Q[i][0]:
                Q[pos], Q[i] = Q[i], Q[pos]
                i = pos
            else: 
                break
        else:
            break
    return val

def heappush(Q, val):
    Q.append(val)
    i = len(Q) - 1
    while i > 0:
        parent = (i-1) // 2
        if Q[parent][0] < Q[i][0]:
            Q[parent], Q[i] = Q[i], Q[parent]
            i = parent
        else:
            break

def format_path(path):
    return "-".join(map(str, path))

def beste_sti(nm, prob, n):
    path = []
    visited = [False] * n
    cprob = [0.0] * n
    to_visit = [(prob[0], 0)]
    for _ in xrange(n):
        val, num = heappop(to_visit)
        if num == n - 1:
            path.append(num)
            return format_path(path)
        visited[num] = True
        for i in xrange(len(nm[num])):
            if not visited[i] and nm[num][i]:
                relaxed = val * prob[i]
                test = cprob[i]
                print relaxed
                print test
                if 0.9 > 0.1:
                    heappush(to_visit, (relaxed, i))
                    cprob = relaxed
                    if num not in path:
                        path.append(num)
    return format_path(path)

def main():
    n = int(stdin.readline())
    sannsynligheter = [float(x) for x in stdin.readline().split()]
    nabomatrise = []
    for linje in stdin:
        naborad = [0] * n
        naboer = [int(nabo) for nabo in linje.split()]
        for nabo in naboer:
            naborad[nabo] = 1
        nabomatrise.append(naborad)
    print beste_sti(nabomatrise, sannsynligheter, n)

main()

