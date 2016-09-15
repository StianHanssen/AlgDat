from itertools import izip

__author__ = 'Stian'
from sys import stdin
from collections import deque

# var ikke definert i den gamle python-versjonen som
# ligger paa noen av stud sine maskine

class Node:
    barn = None
    ratatosk = None
    nesteBarn = None # bare til bruk i DFS
    def __init__(self):
        self.barn = []
        self.ratatosk = False
        self.nesteBarn = -1

def dfs(rot):
    stack = [rot]
    check = []
    while stack:
        node = stack[-1]
        for child in node.barn:
            check.append(child)
        stack.append(check.pop())
    return len(stack)



def bfs(rot):
    rot.nesteBarn = 0
    queue = deque([rot])
    while queue:
        node = queue.popleft()
        if node.ratatosk == 1:
            return node.nesteBarn
        for child in node.barn:
            child.nestebarn = 2
            print child.nesteBarn
            queue.append(child)

funksjon = stdin.readline().strip()
antall_noder = int(stdin.readline())
noder = []
for i in range(antall_noder):
    noder.append(Node())
start_node = noder[int(stdin.readline())]
ratatosk_node = noder[int(stdin.readline())]
ratatosk_node.ratatosk = True
for linje in stdin:
    tall = linje.split()
    temp_node = noder[int(tall.pop(0))]
    for barn_nr in tall:
        temp_node.barn.append(noder[int(barn_nr)])

if funksjon == 'dfs':
    print dfs(start_node)
elif funksjon == 'bfs':
    print bfs(start_node)
elif funksjon == 'velg':
    print bfs(start_node)