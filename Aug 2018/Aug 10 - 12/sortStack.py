class stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        return self.stack.pop()
    def isEmpty(self):
        return len(self.stack) == 0
    def peek(self):
        return self.stack[-1]

def sortStack(a):
    helper = stack()
    while (a.isEmpty() == False):
        curr = a.pop()
        if (helper.isEmpty()):
            helper.push(curr) 
        elif (helper.isEmpty() == False and curr < helper.peek()):
            helper.push(curr)
        else:
            while helper.isEmpty() == False and helper.peek() <= curr:
                poppedNode = helper.pop()
                a.push(poppedNode)
            helper.push(curr)

    return helper

                
 
