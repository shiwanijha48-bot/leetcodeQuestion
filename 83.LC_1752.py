class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        count = 0
        for i in range(0, n):
            if nums[i] > nums[(i+1) % n]:  #%n keeps index inside arrray range
                count += 1
            if count > 1:   # mtlb ki one break, means sorted + rotated
                return False
        return True
        
