


class Node():
    def __init__(self, value=None, next=None):
        self._value = value
        self._next = next

    def getValue(self):
        return self._value

    def getNext(self):
        return self._next

    def setValue(self, new_value):
        self._value = new_value

    def setNext(self, new_next):
        self._next = new_next


class LinkedList():
    def __init__(self):
        self._head = Node()
        self._tail = None
        self._length = 0

    def isEmpty(self):
        return self._head == None

    #add在列表前端添加元素：o(1)
    def add(self, value):
        newnode = Node(value, None)
        newnode.setNext(self._head)
        self._head = newnode
        self._length += 1

    def append(self, value):
        newnode = Node(value)
        if self.isEmpty():
            self._head = newnode
        else:
            current = self._head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(newnode)
            self._length += 1

    def search(self, value):
        current = self._head
        foundvalue = False
        while current != None and not foundvalue:
            if current.getValue() == value
                foundvalue = True
            else:
                current=current.getNext()
        return foundvalue

    def index(self, value):
        current = self._head
        count = 0
        found = None
        while current != None and not found:
            count += 1
            if current.getValue() == value:
                found = True
            else:
                current = current.getNext()
        if found:
            return count
        else:
            raise ValueError('%s is not in linkedlist' %value)

    def remove(self, value):
        current = self._head
        pre = None
        while current != None:
            if current.getValue() == value:
                if not pre:
                    self._head = current.getNext()
                else:
                    pre.setNext(current.getNext())
                break
            else:
                pre = current
                current = current.getNext()

    def insert(self, pos, value):
        if pos <= 1:
            self.add(value)
        elif pos > self._length:
            pass

