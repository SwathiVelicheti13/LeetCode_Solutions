# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        # length of linked lists
        tem = head
        if not head:
            return None
        while tem is not None:
            tem = tem.next
            length+=1
        k = k%length

        # iterated k times and made last value as head in each iteration and removed last value
        curr = head
        prev = None
        for _ in range(k):
            while curr.next is not None:
                prev = curr
                curr = curr.next
                if curr.next is None:
                    temp = head
                    head = curr
                    prev.next = curr.next
                    head.next = temp
                    break
        return head
        