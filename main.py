
from linkedlist import Linked_List
from node import Node
from queue import Queue
from stack import Stack

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

# linked_list.remove_front()



# linked_list.remove_rear()

# for i in linked_list.travers_list():
#     print(i.data)
# newNode = Node(12)

# queue = Queue()
# queue.enqueue(newNode)


# newNode = Node(22)

# queue.enqueue(newNode)
# newNode = Node(242)


# queue.enqueue(newNode)





# newNode = Node(456)
# stack = Stack()
# stack.push(newNode)
# newNode = Node(2345)
# stack.push(newNode)
# newNode = Node(678)
# stack.pop()
# print(stack.pop)

linked_list.insert_after(5,Node(45))
# linked_list.insert_before(Node(15))

for i in linked_list.travers_list():
    print(i.data)



