class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        max_int = 2**31-1 
        rev = 0

        x = abs(x)
        while x > 0:
            last_digit = x % 10
            x //= 10
            if rev > (max_int - last_digit) / 10:
                return 0
            rev = rev * 10 + last_digit

        return sign*rev
