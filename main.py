
from linkedlist import Linked_List
from node import Node


linked_list = Linked_List()

newNode = Node(4)
linked_list.insert_front(newNode)

linked_list.remove_front()
newNode = Node(9)
linked_list.insert_rear(newNode)

newNode = Node(92)
linked_list.insert_rear(newNode)

for i in linked_list.travers_list():
    print(i.data)

linked_list.remove_rear()
