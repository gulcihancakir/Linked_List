from linkedlist import Linked_List
from node import Node


class Queue:
    def __init__(self):
        self.__linked_list = Linked_List()

    def enqueue(self, Node):
        self.__linked_list.insert_rear(Node)

    def dequeue(self):
        return self.__linked_list.remove_front()
