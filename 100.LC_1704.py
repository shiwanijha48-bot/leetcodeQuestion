class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)//2
        count1 = 0
        count2 = 0
        for i in range(n):
            if s[i] in "aeiouAEIOU":
                count1 += 1
            if s[i+n] in "aeiouAEIOU":
                count2 += 1
        if count1 == count2:
            return True
        else:
            return False
