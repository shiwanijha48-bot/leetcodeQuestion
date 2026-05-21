class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(0,n):
            ind = abs(nums[i]) - 1
            if nums[ind] > 0:
                nums[ind] = -nums[ind]
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i+1)
        return res
