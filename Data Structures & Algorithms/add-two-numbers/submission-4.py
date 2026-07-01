# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        dummy = ListNode(-1)
        head = dummy
        p = 1
        while l1 != None:
            n1 += (l1.val * p)
            p *= 10
            l1 = l1.next
        p = 1
        while l2 != None:
            n2 += (l2.val * p)
            p *= 10
            l2 = l2.next
        total = n1 + n2
        if total == 0:
            return ListNode(total)
        while total != 0:
            r = total % 10
            new_node = ListNode(r)
            head.next = new_node
            total = total // 10
            head = head.next
        head = dummy.next
        return head