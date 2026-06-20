class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        return s[:k][::-1] + s[k:]

        
        # s = list(s)
        # l = 0
        # r = k -1
        # while l < r:
        #     s[l], s[r] = s[r], s[l]
        #     l += 1
        #     r -= 1
        # return "".join(s)
