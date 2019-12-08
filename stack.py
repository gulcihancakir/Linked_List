from linkedlist import Linked_List
from node import Node

class Stack(Linked_List):
    def __init__(self):
        self.__linked_list = Linked_List()



    def push(self,Node):
        self.__linked_list.insert_rear(Node)
        return Node 
    
    def pop(self):
        self.__linked_list.remove_rear()
        return  self.__linked_list.remove_rear()
        