from linkedlist import Linked_List
from node import Node

class Stack(Linked_List):
    def __init__(self):
        super().__init__()


    def push(self,Node):
        Linked_List.insert_rear(self,Node)
    
    def pop(self):
        Linked_List.remove_rear(self)