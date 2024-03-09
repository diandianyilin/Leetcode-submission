class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)
        
        result = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in next_greater:
                result[i] = next_greater[nums1[i]]
        
        return result
