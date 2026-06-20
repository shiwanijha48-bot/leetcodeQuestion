class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x = 0 # start
        maxi = 0   # maximum height = ans
        for i in gain:
            x = x + i
            maxi = max(x, maxi)
        return maxi
