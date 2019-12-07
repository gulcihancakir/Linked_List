from node import Node


class Linked_List:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def insertRear(self, Node):

        if self.__head == None:
            self.__head = Node
            self.__tail = Node

        else:
            self.__tail.next = Node
            self.__tail = Node

    def insertFront(self, Node):
        if self.__head == None:
            self.__head = Node
            self.__tail = Node

        else:
            Node.next = self.__head
            self.__head = Node

            return self.__head, self.__tail
        

    def travers_list(self):

        node = self.__head
        while node != None:
            yield node
            node = node.next
