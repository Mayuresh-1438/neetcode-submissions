# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        y = ListNode(-1)
        y.next =  head
        count = 0
        while temp!= None:
            count +=1
            temp = temp.next
        if count == n or count == 1:
            head = head.next
            return head
        it = count - n
        while it>0:
            y = y.next
            it -=1
        y.next = y.next.next
        return head