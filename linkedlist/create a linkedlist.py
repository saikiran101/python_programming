class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

linked_List=LinkedList()
#assign item values
linked_List.head=Node(1)
second=Node(2)
thrid=Node(3)
#connect the nodes
linked_List.head.next=second
second.next=thrid
#print the linkedlist items

while linked_List.head != None:
    print(linked_List.head.item, end="->")
    linked_List.head=linked_List.head.next

