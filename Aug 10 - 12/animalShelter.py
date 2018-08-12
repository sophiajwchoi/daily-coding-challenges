#animalShelter Question


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.order = None
        self.type = species
    def setOrder(self,order):
        self.order = order
    def getOrder(self):
        return self.order
    def compareOrderThan(self, a):
        return self.order > a.order

from collections import deque
class AnimalShelterQ:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0
    def enqueue(self, animal):
        animal.setOrder(self.order)
        self.order += 1

        if (animal.type == 0):
            self.dogs.append(animal)
        else:
            self.cats.append(animal)

    def dequeueAny(self):
        if (len(self.dogs) == 0):
             return self.dequeueCat()
        elif (len(self.cats) == 0):
            return self.lendequeueDog()
        else:

            a = self.peek(0)
            b = self.peek(1)
            if (a.getOrder() < b.getOrder()):
                return a
            else:
                return b
    def peek(self, species):
        if species == 0:
            return self.dogs[0]
        else:
            return self.cats[0]
    def dequeueDog(self):
        return self.dogs.popleft()
    def dequeueCat(self):
        return self.cats.popleft()
