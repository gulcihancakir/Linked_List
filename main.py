
from linkedlist import Linked_List
from node import Node


a = Linked_List()
a.head = Node(1)
x = Node(2)
y = Node(3)

a.head.next = x
x.next = y
b=a.travers_list()
for i in b:
    print(i.data)






