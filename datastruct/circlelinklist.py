

# https://www.cnblogs.com/wgDream/p/7525966.html
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


class CycleLinkList():
    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        return self.__head is None

    def length(self):
        if self.is_empty():
            return 0
        current = self.__head
        count = 1

        while current.next != self.__head:
            count += 1
            current = current.next
        return count

    def linklistPrint(self):
        if self.is_empty():
            print("")
            return

        current = self.__head

        while current.next != self.__head:
            print(current.item, end = " ")
            current = current.next

        print(current.item, end= " ")
        print("")

    def addBegin(self, item):
        node = Node(item)
        if self.is_empty():
            node.next = node
            self.__head = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            self.__head = node
            cur.next = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.__head = node
            node.next = node
        else:
            cur = self.__head
            while cur.next != self.__head:
                cur = cur.next
            node.next = self.__head
            cur.next = node


    def insert(self, pos, item):
        if pos <= 0:
            self.addBegin(item)
        elif pos >= self.length():
            self.append(item)
        else:
            cur = self.__head
            count = 0
            while count < (pos-1):
                count += 1
                cur = cur.next
            node = Node(item)
            node.next = cur.next
            cur.next = node


    def remove(self, item):

        if self.is_empty():
            return
        cur = self.__head
        pre = None

        while cur.next != self.__head:
            if cur.item == item:
                if cur == self.__head:
                    rel = self.__head
                    while rel.next != self.__head:
                        rel = rel.next
                    self.__head = cur.next
                    rel.next = self.__head
                else:
                    pre.next = cur.next
                return
            pre = cur
            cur = cur.next

        if cur.item == item:
            if pre:
                pre.next = self.__head
            else:
                self.__head = None


    def search(self, item):
        cur = self.__head
        while cur.next != self.__head:
            if cur.item == item:
                return True
            cur = cur.next
        if cur.item == item:
            return True
        return False


if __name__ == '__main__':
    link = CycleLinkList()
    print(link.is_empty())

    link.append(9)
    print(link.length())
    link.linklistPrint()

    link.append(0)
    print(link.length())
    link.linklistPrint()


    link.addBegin(8)
    print(link.length())
    link.linklistPrint()

    link.addBegin(7)
    print(link.length())
    link.linklistPrint()

    link.insert(0, 5)
    link.linklistPrint()

    link.insert(10, 6)
    link.linklistPrint()

    link.insert(2, 3)
    link.linklistPrint()

    link.remove(6)
    link.linklistPrint()

    link.remove(5)
    link.linklistPrint()

    link.remove(3)
    link.linklistPrint()

