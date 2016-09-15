from sys import stdin

def find_num_paths(C, sources, terminators):
    end = min(len(sources), len(terminators))
    c_m, n = modify_matrix(C, sources, terminators)
    F = [[0 for i in xrange(n)] for j in xrange(n)]
    paths = 0
    source = 0
    terminator = n - 1
    while True:
        path = finnFlytsti(source, terminator, F, c_m)
        if path is None:
            return paths
        paths += 1
        if paths == end:
            return paths
        for i in xrange(len(path) - 1):
            F[path[i]][path[i + 1]] += 1
            F[path[i + 1]][path[i]] -= 1

def modify_matrix(C, sources, terminators):
    n = len(C)
    size = n * 2 + 2
    adj_matrix = [[0 for _ in xrange(size)] for _ in xrange(size)]
    [assign_val(adj_matrix, 0, (start * 2) + 1, 1) for start in sources]
    [[assign_val(adj_matrix, (i + 1) * 2, (j * 2) + 1, C[i][j]) for j in xrange(n)] for i in xrange(n)]
    [assign_val(adj_matrix, (i * 2) + 1, (i + 1) * 2, 1) for i in xrange(n)]
    [assign_val(adj_matrix, (end + 1) * 2, size - 1, 1) for end in terminators]
    return adj_matrix, size

def assign_val(M, pos1, pos2, val):
    M[pos1][pos2] = val

def finnFlytsti(kilde, sluk, F, C):
    n = len(F)
    oppdaget = [False] * n
    forelder = [None] * len(F)
    koe = [kilde]
    while koe:
        node = koe.pop(0)
        if node == sluk:
            # Har funnet sluken, lager en array med passerte noder
            sti = []
            i = node
            while True:
                sti.append(i)
                if i == kilde:
                    break
                i = forelder[i]
            sti.reverse()
            return sti;
        for nabo in range(n):
            if not oppdaget[nabo] and F[node][nabo] < C[node][nabo]:
                koe.append(nabo);
                oppdaget[nabo] = True;
                forelder[nabo] = node;
    return None

def main():
    stdin.readline()
    startrom = [int(x) for x in stdin.readline().split()]
    utganger = [int(x) for x in stdin.readline().split()]
    nabomatrise = []
    for linje in stdin:
        naborad = [int(nabo) for nabo in linje.split()]
        nabomatrise.append(naborad)
    print find_num_paths(nabomatrise, startrom, utganger)

main()
