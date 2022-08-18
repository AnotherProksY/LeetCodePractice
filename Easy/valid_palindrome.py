class Solution:
    def isPalindrome(self, s: str) -> bool:
        optW = ''.join([ c for c in s if c.isalnum() ])
        return optW.lower() == optW.lower()[::-1]