# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c=head
        count=0

        while c:
            count+=1
            c=c.next
        x = count - n

        if count==n:
            head=head.next
            return head

        if count>=2:
            p=head
            for i in range(1,x):
                p=p.next
            p.next=p.next.next
            return head
        else:
            head=None
            return head
  

        