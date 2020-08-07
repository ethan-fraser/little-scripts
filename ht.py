from random import randint

class LinkedList:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self, value):
        self.first = self.Node(value)
        self.size = 1

    def add(self, value):
        current = self.first
        while (current.next):
            current = current.next
        current.next = self.Node(value)
        self.size += 1

    def print(self):
        print("[", end='')
        current = self.first
        while (current.next):
            print(str(current.value) + ", ", end='')
            current = current.next
        print(str(current.value) + "]", end='')


class HashTable:
    def __init__(self, capacity, p, a=None, b=None):
        self.items = [None for i in range(capacity)]
        self.capacity = capacity
        if (a and b):
            self.a = a
            self.b = b
        else:
            self.a = randint(0, 10000)
            self.b = randint(0, 10000)
        self.p = p

    def insert(self, item):
        h = self.hash(item)
        full = True
        collisions = 0
        while (full):
            if self.items[h] == None:
                full = False
                self.items[h] = LinkedList(item)
            else:
                self.items[h].add(item)
            return h

    def print(self):
        print("[", end='')
        for i in range(len(self.items)):
            if self.items[i] == None:
                print("None", end='')
            else:
                self.items[i].print()
            if i < len(self.items)-1:
                print(", ", end='')
        print("]")

    def search(self, item):
        pass

    def remove(self, item):
        pass

    def hash(self, value):
        return (((value * self.a) + self.b) % self.p) % self.capacity


if __name__ == "__main__":
    a = [8, 22, 36, 75, 61, 13, 83, 58]
    h = HashTable(11, 101, 6, 10)
    for x in a:
        h.insert(x)
    h.print()

    print()

    h2 = HashTable(11, 101)
    for x in a:
        h2.insert(x)
    h2.print()
