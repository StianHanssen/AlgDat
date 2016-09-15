__author__ = 'Stian'

nabomatrise = [[0, 1, 1, 0, 0, 0],
               [0, 0, 0, 1, 0, 0],
               [0, 0, 0, 1, 1, 0],
               [0, 0, 0, 0, 0, 1],
               [0, 1, 0, 1, 0, 1],
               [0, 0, 0, 1, 0, 0]]
n = 6
nodesInverted = [0, 1, 2, 4]
values = [1,2,3,1,2,4,5,6,3,2,1]
nodes = [i for i in xrange(len(values)) if values[i] == 1]
#for line in text:
#    for symbol in line:
#        arrayLine.append(symbol)
#    matrix.append(arrayLine)
#[matrix.append([line]) for line in text for symbol in line]
print(nodes)
print([i for i in xrange(n)])
print([i for i in xrange(n) if i not in nodes])
print(sum(1 for i in xrange(n) if i not in nodes))
print(sum(nabomatrise[j][k] for j in nodesInverted for k in nodesInverted))

text = "011000\n000100\n000110\n000001\n010101\n000100"
matrix = [map(int, stdin.readline()) for i in xrange(0, n)]
myList = map(int, something)
print(myList)
