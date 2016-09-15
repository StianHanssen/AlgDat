from sys import stdin


def sub_graph_density(adj_matrix, startnode, n):
    stack = set(startnode)
    nodes = map(None, xrange(n))
    nodes.remove(startnode)
    def doeet(x):
        nodes.remove(x)
        stack.add(x)
    while stack:
        line = adj_matrix[stack.pop()]
        [doeet(i) for i in xrange(len(line)) if line[i] and i in nodes]
    if len(nodes) == 0:
        return 0.0
    else:
        edges = sum(1 for i in nodes for j in nodes if adj_matrix[i][j] == 1)
        return float(edges) / float(len(nodes) ** 2)


def main():
    n = int(stdin.readline())
    adj_matrix = [map(int, stdin.readline().strip()) for i in xrange(0, n)]
    for line in stdin:
        print "%.3f" % (sub_graph_density(adj_matrix, int(line), n) + 1E-12)


main()
