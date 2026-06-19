class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort() # sort arr in asc ordr
        res = 0
        for i in range(0, len(nums), 2):
            res += nums[i]  # adding smallest elment of each pair
        return res
