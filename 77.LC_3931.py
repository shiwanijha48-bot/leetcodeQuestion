class Solution:
    def isAdjacentDiffAtMostTwo(self, s: str) -> bool:
        n = len(s)
        for i in range(0, n-1):
            k = int(s[i]) - int(s[i+1])
            if abs(k) > 2:
                return False
        return True
