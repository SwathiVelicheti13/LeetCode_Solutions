# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        temp = head
        slow = temp
        fast = temp.next

        while fast and fast.next is not None:
            slow = slow.next
            fast=fast.next.next
            if fast == slow:
                return True
        return False
        

        