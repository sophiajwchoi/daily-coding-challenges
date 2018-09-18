class queueAsStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, item):
        self.stack1.append(item)
    def pop(self):
        while(len(self.stack1) != 0):
            poppedNode = self.stack1.pop()
            self.stack2.append(poppedNode)
        return self.stack2.pop()
