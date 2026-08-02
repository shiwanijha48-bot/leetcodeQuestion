# 160.LC_216.py
class Solution:
    def func(self, n, Sum, last, nums, k, ans):
        # Base case: Found valid combination
        if Sum == n and len(nums) == k:
            ans.append(list(nums))  # Make a copy to preserve state
            return
        # Pruning: Early termination for invalid paths
        if Sum > n or len(nums) > k:
            return
        # Try numbers from last to 9 (ascending order, no duplicates)
        for i in range(last, 10):
            nums.append(i)
            self.func(n, Sum + i, i + 1, nums, k, ans)  # Update sum and next start
            nums.pop()  # Backtrack

    def combinationSum3(self, k, n):
        ans = []
        nums = []
        self.func(n, 0, 1, nums, k, ans)  # Start with sum=0, last=1
        return ans


'''
216. Combination Sum III
Solved
Medium
Topics
premium lock icon
Companies
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.

 

Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.
Example 2:

Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.
Example 3:

Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9], the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1, there are no valid combination.
 

Constraints:

2 <= k <= 9
1 <= n <= 60


'''
