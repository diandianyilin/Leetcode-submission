class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        char_count = {}
        
        # Count the occurrences of each character in magazine
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Check if ransomNote can be constructed
        for char in ransomNote:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1
        
        return True