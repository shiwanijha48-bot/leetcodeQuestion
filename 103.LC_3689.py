class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        mini = min(nums)  # smallest in arr
        maxi = max(nums)  # largest in arr
        return k * (maxi - mini)  # max subarr val = global max - global min
        # since the same subarray can be chosen k times, so multiply it by k 
