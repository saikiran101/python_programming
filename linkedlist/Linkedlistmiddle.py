from LinkedlistHelper import LinkedList
l=LinkedList()
head=l.arrayToList([1,2,3,4,5])
def printmiddle(head):
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
    print(slow.val)
printmiddle(head)