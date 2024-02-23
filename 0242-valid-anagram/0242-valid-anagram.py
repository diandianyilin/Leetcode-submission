class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of s and t are equal
        if len(s) != len(t):
            return False

        # Create dictionaries to store character frequencies
        s_dict = {}
        t_dict = {}

        # Iterate through each character in s and t
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1

        for char in t:
            t_dict[char] = t_dict.get(char, 0) + 1

        # Compare the dictionaries
        return s_dict == t_dict
