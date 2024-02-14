class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Remove trailing spaces from the string
        s = s.rstrip()

        # Split the string into words
        words = s.split()

        # Check if there are any words in the string
        if not words:
            return 0

        # Return the length of the last word
        return len(words[-1])
