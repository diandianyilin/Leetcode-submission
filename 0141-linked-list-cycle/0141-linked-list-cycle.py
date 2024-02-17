class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Initialize two pointers, slow and fast
        slow = head
        fast = head

        # Move slow by one step and fast by two steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If slow and fast meet, there is a cycle
            if slow == fast:
                return True

        # If there is no cycle, fast will reach the end of the list
        return False
