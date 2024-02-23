class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Helper function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            curr = node
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        # Base case: empty list or single node list
        if not head or not head.next:
            return True

        # Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the linked list
        second_half = reverseLinkedList(slow)

        # Compare the values of the first half and the reversed second half
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next

        return True
