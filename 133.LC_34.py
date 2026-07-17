class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def low_b(nums,target):
            n = len(nums)
            lb = -1
            low = 0
            high = n-1
            while low <= high:
                mid = (low + high)//2
                if nums[mid] >= target:
                    if nums[mid] == target:
                        lb = mid
                    high = mid -1
                else:
                    low =  mid + 1
            return lb
        def upp_b(nums,target):
            n = len(nums)
            ub = -1
            low = 0
            high = n-1
            while low <= high:
                mid = (low + high)//2
                if nums[mid] > target:
                    ub = mid
                    high = mid -1
                else:
                    low = mid + 1
            return ub
        lb = low_b(nums,target)
        if lb == -1:
            return [-1,-1]
        ub = upp_b(nums, target)
        if ub == -1:
            return [lb,len(nums)-1]
        return [lb,ub-1]



'''

34. Find First and Last Position of Element in Sorted Array
Solved
Medium
Topics
premium lock icon
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

'''
