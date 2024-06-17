# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create dummy node and point it to head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            # Identify nodes to be swapped
            first = prev.next
            second = prev.next.next
            # Perform swap
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
        return dummy.next


