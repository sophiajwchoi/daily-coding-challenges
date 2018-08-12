class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def identical(sNode, tNode):
    if (sNode == None and tNode == None):
        return True
    if (sNode == None or tNode == None):
        return False

    return (sNode.data == tNode.data and identical(sNode.left, tNode.left) and identical(sNode.right, tNode.right))
            

def isSubtree(tNode, sNode):
    if sNode is None or tNode is None:
        return True
    if (identical(sNode, tNode)):
        return True
    return isSubtree(tNode.left, sNode) or isSubtree(tNode.right, sNode)
