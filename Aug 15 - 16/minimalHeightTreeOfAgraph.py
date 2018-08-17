class Node:
    def __init__(self, val):
        self.val = val
        self.adj = []
    def add_edge(self, edge_to):
        self.adj.append(edge_to)

def minimal_height_tree(n, edges):
    vert = set()
    for x, y in edges:
            x = Node(x)
            y = Node(y)
            vert.add(x)
            vert.add(y)
            x.add_edge(y)
    heightMap = {}
    for x in vert:
        heightMap[x] = getHeight(x)
    return min(heightMap, key = heightMap.get)


def getHeight(root):
    if root == None:
        return 0
    return 1 + max(getHeight(root.adj[i]) for i in range(len(root.adj)))    
    
