# Definition for singly-linked list.
from LinkedlistHelper import LinkedList
l=LinkedList()
head=l.arrayToList([1,2,2,1])
def isPalindrome(head):
        result=[]
        while head != None:
            result.append(head.val)
            head=head.next
        if result==result[::-1]:
            return True   
        return False
isPalindrome(head)