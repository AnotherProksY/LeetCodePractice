class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        rev = sign * int(str(x)[::-1])
        
        if rev < pow(-2, 31) or rev > pow(2, 31)-1:
            return 0
        else:
            return rev