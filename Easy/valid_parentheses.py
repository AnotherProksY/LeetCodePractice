class Solution:
    def isValid(self, s: str) -> bool:
        # Open brackets position
        om = []

        # Close brackets mapping
        cm = {
            ')':'(',
            ']':'[',
            '}':'{',
        }

        for b in s:
            if b in '([{':
                om.append(b)
            else:
                if om and cm[b] == om[-1]:
                    om.pop(-1)
                else:
                    return False
            
        if not om:
            return True
        else:
            return False
