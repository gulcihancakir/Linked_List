from node import Node


class Linked_List:
    def __init__(self):
        self.__head = None
        self.__tail = None

    def insert_front(self, Node):
        if self.__head == None:
            self.__head = Node
            self.__tail = Node

        else:
            Node.next = self.__head
            self.__head = Node

    def remove_front(self):

        if self.__head != None:
            temp = self.__head
            q = self.__head
            self.__head = q.next
            q = None

            return temp.data

    def insert_rear(self, Node):

        if self.__head == None:
            self.__head = Node
            self.__tail = Node

        else:
            self.__tail.next = Node
            self.__tail = Node

    def remove_rear(self):
        for i in self.travers_list():
            if i.next == self.__tail:
                q = i.next
                i.next = None
                self.__tail = i

                return q.data

    def insert_before(self, link, Node):

        pass

    def remove_before(self):
        pass

    def insert_after(self, link, Node):
        for i in self.travers_list():
            if i.data == link:
                temp = i.next

                Node.next = temp
                i.next = Node

    def remove_after(self, link):

        pass

    def travers_list(self):

        node = self.__head
        while node != None:
            yield node
            node = node.next
