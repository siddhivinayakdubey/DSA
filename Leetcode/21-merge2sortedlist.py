from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p = list1
        q = list2
        if p and not q:
            return p
        if q and not p:
            return q
        if p and q:
            if p.val < q.val:
                head = p
                p = p.next
            else:
                head = q
                q = q.next

            r = head

            while p and q:
                if p.val < q.val:
                    r.next = p
                    r = r.next
                    p = p.next
                else:
                    r.next = q
                    r = r.next
                    q = q.next

            if p:
                r.next = p
            if q:
                r.next = q

            return head
        return None


