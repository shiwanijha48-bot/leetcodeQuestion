class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()  # Sort the array in ascending order
        n = len(nums)
        smallestSum = 0
        largestSum = 0
        for i in range(0, k):  # sum of k smallest elements
            smallestSum += nums[i]
        for j in range(n-k, n):   # sum of k largest elements
            largestSum += nums[j]
        return abs(largestSum - smallestSum)
