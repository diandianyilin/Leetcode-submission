# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the result linked list
        dummy = ListNode(0)
        current = dummy
        carry = 0

        # Iterate through the two linked lists
        while l1 or l2:
            # Get the values of the current nodes, or 0 if the nodes are None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Calculate the sum of the current digits and the carry
            sum = val1 + val2 + carry

            # Update the carry
            carry = sum // 10

            # Create a new node with the sum % 10 as its value
            current.next = ListNode(sum % 10)

            # Move to the next nodes in the linked lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

            # Move to the next node in the result linked list
            current = current.next

        # If there is still a carry after iterating through the linked lists, create a new node for it
        if carry > 0:
            current.next = ListNode(carry)

        # Return the head of the result linked list (excluding the dummy node)
        return dummy.next
