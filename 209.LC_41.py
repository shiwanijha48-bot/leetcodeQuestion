class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = max(nums)
        if maxi < 1:
            return 1
        for i in range(1, maxi +2):
            if i not in s:
                return i
#  Method - 2
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = max(nums)
        if maxi < 1:
            return 1
        for i in range(1, maxi +2):
            if i not in s:
                return i

#  used set as it is easy to look in it, tc = o(1) for searching elment in set.

# maxi + 2 is used because range() excludes the ending value.
# We need to check up to maxi + 1, because if all numbers from 1 to maxi are present, then maxi + 1 will be the smallest missing positive.

'''
41. First Missing Positive
Solved
Hard
Topics
premium lock icon
Companies
Hint
Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

 

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
 

Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
'''
