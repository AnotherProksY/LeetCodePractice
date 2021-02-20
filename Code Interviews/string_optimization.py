class Solution:
    def optimizeString(self, s: str) -> str:
        if not len(s): return ""

        counter = 0
        result = s[0]

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                counter += 1
            else:
                if counter:
                    result += str(counter)

                result += s[i]
                counter = 0

        if counter:
            result += str(counter)

        return result
