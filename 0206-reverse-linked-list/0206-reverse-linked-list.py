# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize previous and current pointers
        prev = None
        current = head

        # Iterate through the linked list
        while current:
            # Store the next node
            next_node = current.next

            # Reverse the link
            current.next = prev

            # Move the pointers to the next nodes
            prev = current
            current = next_node

        # Return the new head of the reversed linked list
        return prev
