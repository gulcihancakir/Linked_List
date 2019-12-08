
from linkedlist import Linked_List
from node import Node


linked_list = Linked_List()

newNode = Node(4)
linked_list.insert_front(newNode)
newNode = Node(5)
linked_list.insert_front(newNode)
newNode = Node(6)
linked_list.insert_front(newNode)

newNode = Node(7)
linked_list.insert_rear(newNode)
newNode = Node(8)
linked_list.insert_rear(newNode)
newNode = Node(9)
linked_list.insert_rear(newNode)

linked_list.remove_front()

linked_list.remove_rear()

for i in linked_list.travers_list():
    print(i.data)

