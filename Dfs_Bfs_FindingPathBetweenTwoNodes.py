class Node:
    def __init__(self, name):
        self.name = name
        self.adj = []
        self.visited = False

##class Graph:
##    def __init__(self):
##        self.nodes = []
##

def dfsSearch(node1, node2):
    if (node1 == None or node2 == None):
        return
    if (node1 == node2):
        print("Found")
    node1.visited = True
    for node in node1.adj:
        if node.visited == False:
            dfsSearch(node, node2)

from collections import deque

def bfsSearch(node1, node2):
    if (node1 == None or node2 == None):
        return
    queue = deque()
    node1.visited = True
    queue.append(node1)

    while(len(queue)!= 0):
        node = queue.popleft()
        if (node == node2):
            print("Found")
        for x in node.adj:
            if x.visited == False:
                x.visited = True
                queue.append(x)

def main():
    a = Node("sophia")
    b = Node("Hello")
    c = Node("BI")
    d = Node("dfd")
    e = Node("23")
    f = Node("wefw")
    a.adj.append(b)
    b.adj.append(c)
    c.adj.append(d)
    d.adj.append(e)
    e.adj.append(f)
    bfsSearch(a, f)
