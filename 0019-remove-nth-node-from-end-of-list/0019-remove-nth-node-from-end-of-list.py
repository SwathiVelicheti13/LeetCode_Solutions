# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        length = 0
        curr = head
        while curr:
            length = length+1
            curr = curr.next

        ct = length-n

        dummy = ListNode()
        dummy.next = head

        temp = dummy
        count = 0
        while temp:
            if count == ct:
                temp.next = temp.next.next

            count+=1
            temp = temp.next
        return dummy.next
        

        # prev = None
        # curr = head

        # while curr:
        #     n_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = n_node

        # temp = prev
        # count = 0
         
        # prev_head = None
        # dummy = ListNode()

        # dummy.next = prev

        # temp = dummy

        # while temp:
        #     if count == n:
        #         print(count)
        #         prev_head.next = temp.next
        #     count+=1
        #     prev_head = temp
        #     temp=temp.next

        # rev = None
        # curr = prev

        # while curr:
        #     n_node = curr.next
        #     curr.next = rev
        #     rev = curr
        #     curr = n_node

        
        # return rev
            


        