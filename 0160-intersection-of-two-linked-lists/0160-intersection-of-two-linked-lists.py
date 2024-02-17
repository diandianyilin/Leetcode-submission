class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Calculate the lengths of both lists
        lenA, lenB = 0, 0
        currA, currB = headA, headB
        while currA:
            lenA += 1
            currA = currA.next
        while currB:
            lenB += 1
            currB = currB.next

        # Adjust the starting point of the longer list
        if lenA > lenB:
            for _ in range(lenA - lenB):
                headA = headA.next
        else:
            for _ in range(lenB - lenA):
                headB = headB.next

        # Traverse both lists simultaneously to find the intersection point
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        # No intersection found
        return None
