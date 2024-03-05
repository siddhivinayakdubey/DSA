def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    f = ListNode(0)
    result = f
    carry = 0
    while l1 or l2:
        if l1:
            x = l1.val
        else:
            x = 0
        if l2:
            y = l2.val
        else:
            y = 0
        temp = x + y + carry
        if temp >= 10:
            f.next = ListNode(temp % 10)
            carry = temp // 10
        else:
            f.next = ListNode(temp)
            carry = 0
        f = f.next
        if l1.next:
            l1 = l1.next
        if l2.next:
            l2 = l2.next

    if carry == 1:
        f.next = ListNode(carry)

    return result.next