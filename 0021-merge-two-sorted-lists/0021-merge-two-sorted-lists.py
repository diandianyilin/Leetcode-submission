class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to serve as the head of the merged list
        dummy = ListNode(0)
        # Create a pointer to keep track of the current node in the merged list
        current = dummy

        # Iterate through both lists while they are not empty
        while list1 and list2:
            # Compare the values of the current nodes in list1 and list2
            if list1.val <= list2.val:
                # If the value in list1 is smaller or equal, add it to the merged list
                current.next = list1
                # Move the pointer in list1 to the next node
                list1 = list1.next
            else:
                # If the value in list2 is smaller, add it to the merged list
                current.next = list2
                # Move the pointer in list2 to the next node
                list2 = list2.next
            # Move the pointer in the merged list to the next node
            current = current.next

        # If there are any remaining nodes in list1 or list2, add them to the merged list
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        # Return the head of the merged list (excluding the dummy node)
        return dummy.next
