class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        zeros = nums.count(0)
        for i in range(n-1, n- zeros-1 , -1):
            if nums[i] != 0 :
                ans += 1
        return ans
