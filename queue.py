from linkedlist import Linked_List
from node import Node


class Queue(Linked_List):
    def __init__(self):
        super().__init__()

    def enqueue(self, Node):
        Linked_List.insert_rear(self, Node)

    def dequeue(self):
        Linked_List.remove_front(self)
