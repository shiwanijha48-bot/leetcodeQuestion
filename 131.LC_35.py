class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        h = n - 1
        ans = n  # default insert position = end
        while l <= h:
            mid = (l+ h)// 2  # midpoint of the window
            if nums[mid] >= target: 
                ans = mid # nums[mid] is a valid (or exact position
                h = mid - 1  # keep searching left half
            else:  # nums[mid] < target
                l = mid + 1 # search right half
        return ans # final insertion index

#  TC = O(log n)

'''
35. Search Insert Position
Solved
Easy
Topics
premium lock icon
Companies
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104


'''
