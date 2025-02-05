# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
    
       
    
        # Push the first node of each list into the heap with index
        for i, l in enumerate(lists):
            if l:
                heappush(heap, (l.val, i, l))  # Store (value, index, node)
        
        dummy = ListNode()  # Dummy node to simplify list operations
        current = dummy
        
        while heap:
            _, i, smallest = heappop(heap)  # Get the smallest node
            current.next = smallest  # Append to merged list
            current = current.next  # Move forward
            
            if smallest.next:  # If more nodes exist in that list, push next node
                heappush(heap, (smallest.next.val, i, smallest.next))  # Keep index for uniqueness
        
        return dummy.next  # Return the merged list
                