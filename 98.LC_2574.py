class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        left = 0
        res = []
        for i in nums:
            right = total - left - i
            res.append(abs(left-right))
            left += i
        return res
