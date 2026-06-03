class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        s =str(n)
        freq = {}
        res = 0
        for i in s:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i in freq:
            res += int(i)* freq[i]
        return res

