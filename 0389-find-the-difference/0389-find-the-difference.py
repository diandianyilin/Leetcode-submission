class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = {}
        
        # Count the occurrences of each character in string s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Subtract the occurrences of each character in string t
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return char
            char_count[char] -= 1
        
        return ""  # Return an empty string if no extra character is found