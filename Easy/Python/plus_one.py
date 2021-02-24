class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_d = [str(d) for d in digits]
        l_int = int("".join(str_d))+1
        output = []

        for i in range(len(str(l_int))):
            output.append(int(str(l_int)[i]))
            
        return output