# coding=utf-8


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    # 打印列表中的元素
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

    # 从头部添加元素
    def addBegin(self, newdata):
        newnode = Node(newdata)
        newnode.nextval = self.headval
        self.headval = newnode

    # 在尾部添加元素
    def addEnd(self, newdata):
        newnode = Node(newdata)
        if self.headval is None:
            self.headval = newnode
            return
        last = self.headval
        while last.nextval:
            last = last.nextval
        last.nextval = newnode

    # 在中间插入元素
    def insert(self, middle_node, newdata):
        if middle_node is None:
            print('The mentioned node is absent')
            return
        newnode = Node(newdata)
        newnode.nextval = middle_node.nextval
        middle_node.nextval = newnode

    # 删除结点
    def removeNode(self, value):
        head = self.headval
        if (head is not None):
            if (head.dataval == value):
                self.headval = head.nextval
                head = None
                return
        while(head is not None):
            if head.dataval == value:
                break
            prev = head
            head = head.nextval

        if (head == None):
            return

        prev.nextval = head.nextval
        head = None





list = SLinkedList()
list.headval = Node('Mon')
e2 = Node('Tue')
e3 = Node('Weds')

list.headval.nextval = e2
e2.nextval = e3

list.addBegin('Sun')
list.addEnd('Thr')

list.insert(e2, "Fri")

#list.removeNode('Tue')

list.listprint()
