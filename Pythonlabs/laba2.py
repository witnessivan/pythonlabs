

class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first != None:
            current = self.first
            out = 'Двухсвязный список [' + str(current.value)
            while current.next != None:
                current = current.next
                out += ',' + str(current.value)
            return out + ']'
        return 'Двухсвязный список []'

    def clear(self):
        self.__init__()

    def add(self, val):
        a = Node(val, None, self.last)
        if (self.last != None):
            self.last.next = a
        if (self.first == None):
            self.first = a
        self.last = a

f = open('addfile.txt','r')
a = f.read()
a.split(',')
print(a)
z = LinkedList()
z.add(a)
print(z)
