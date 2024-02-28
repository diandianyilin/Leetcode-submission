class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_pointer = 0
        t_pointer = 0
        
        # Iterate through both strings
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
            t_pointer += 1
        
        # Check if all characters in s have been found in t
        return s_pointer == len(s)