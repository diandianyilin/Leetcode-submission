class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Check if needle is an empty string
        if not needle:
            return 0

        # Check if needle is longer than haystack
        if len(needle) > len(haystack):
            return -1

        # Iterate through the haystack
        for i in range(len(haystack) - len(needle) + 1):
            # Check if the substring starting from index i matches the needle
            if haystack[i:i+len(needle)] == needle:
                return i

        # If needle is not found, return -1
        return -1
