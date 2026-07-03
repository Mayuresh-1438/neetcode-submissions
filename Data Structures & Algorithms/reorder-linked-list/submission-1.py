# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None:
            return None
        slow , fast = head,head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        head1 = head
        head2 = slow.next
        slow.next = None
        curr = head2
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head2 = prev
        n1 = head1.next
        n2 = head2.next
        while n2 != None:
            head1.next = head2
            head2.next = n1
            head1 = n1
            head2 = n2
            n1 = n1.next
            n2 = n2.next
        head1.next = head2
        head2.next = n1

