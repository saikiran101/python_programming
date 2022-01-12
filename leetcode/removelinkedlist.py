from LinkedlistHelper import LinkedList
class Solution:
    def removeElements(self, head, val: int):
        if head==None:
            return head
        prev,curr=None,head
        while curr!=None:
            if curr.val==val:
                if prev==None:
                    head=curr.next
                else:
                    prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return head

s=Solution()
l=LinkedList()
List=l.arrayToList([1,2,3,2,5])
res=s.removeElements(List,2)
print(res)