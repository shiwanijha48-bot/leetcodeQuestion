class Solution:
    def maxPower(self, s: str) -> int:
        res = 1
        i = 1
        for j in range(1, len(s)):
            if s[j] == s[j-1]:
                i += 1
            else:
                i = 1
            res = max(res, i)
        return res
