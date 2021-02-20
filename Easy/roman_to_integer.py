class Solution:
    def romanToInt(self, s: str) -> int:
        r_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        num = [r_map[i] for i in s]
        
        for i in range(len(num)):
            try:
                if num[i] < num[i+1]:
                    num[i] = num[i+1]-num[i]
                    del num[i+1]
            except IndexError:
                continue
                
        return sum(num)