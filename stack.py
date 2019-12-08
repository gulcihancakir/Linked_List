from linkedlist import Linked_List
from node import Node


class Stack:
    def __init__(self):
        self.__linked_list = Linked_List()

    def push(self, Node):
        self.__linked_list.insert_rear(Node)

    def pop(self):
        return self.__linked_list.remove_rear()
