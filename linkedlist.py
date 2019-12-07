from node import Node


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertRear(self, Node):

        if self.head == None:
            self.head = Node
            self.tail = Node

        else:
            self.tail.next = Node
            self.tail = Node

    def insertFront(self, Node):
        if self.head == None:
            self.head = Node
            self.tail = Node

        else:
            Node.next = self.head
            self.head = Node

            return self.head, self.tail

    def travers_list(self):

        node = self.head
        while node != None:
            yield node
            node = node.next
