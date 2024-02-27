class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        
        # Count the occurrences of each character in the string
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Find the index of the first non-repeating character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        return -1  # Return -1 if no non-repeating character is found