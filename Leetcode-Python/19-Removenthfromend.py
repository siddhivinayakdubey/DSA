# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        if count >= 2:
            x = count - n + 1
            p = head
            if x == 1:
                head = p.next
            else:

                for i in range(0, x - 2):
                    p = p.next
                p.next = p.next.next
            return head
        else:
            head = None
            return head
