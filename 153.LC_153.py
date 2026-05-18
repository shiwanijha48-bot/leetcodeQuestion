class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(0, n-1):   # traverse arr
            if nums[i] > nums[i+1]:   # curr ele is greater than next
                return nums[i+1]  # next ele is min
        return nums[0]  # if not roation, 1st ele is min

# -----------------------------------------------------------------------
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
