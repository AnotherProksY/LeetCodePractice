class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        
        strs.sort(key=len)
        prf = strs[0]
        for w in strs[1:]:
            prf2 = ''
            for i, c in enumerate(w[:len(prf)]):
                if c == prf[i]: prf2 += c
                else: break
 
            prf = prf2 
            
        return prf
