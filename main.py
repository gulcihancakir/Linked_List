
from linkedlist import Linked_List
from node import Node


linked_list = Linked_List()

newNode = Node(4)
linked_list.insertFront(newNode)

newNode = Node(9)
linked_list.insertRear(newNode)

for i in linked_list.travers_list():
    print(i.data)
