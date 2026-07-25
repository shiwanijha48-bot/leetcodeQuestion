class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total_subsets = 1<<n
        result = []
        for num in range(0,total_subsets):
            lst = []
            for i in range(0,n):
                if (num & (1<<i))!= 0:
                    lst.append(nums[i])
            result.append(lst)
        return result
        #  tc = o(n * 2^n),  sc = o(2^n * n)

'''
78. Subsets
Solved
Medium
Topics
premium lock icon
Companies
Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

 

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
 

Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.

'''
