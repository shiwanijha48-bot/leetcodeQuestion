class Solution:
    def backtrack(self, subset, index, target, result, candidates):
        if target == 0:
            result.append(subset.copy()) 
            return
        for i in range(index, len(candidates)):
            if i > index and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > target:
                break
            subset.append(candidates[i])
            self.backtrack(subset, i + 1, target - candidates[i], result, candidates)
            subset.pop()

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # Sort to enable duplicate skipping and early termination
        result = []
        self.backtrack([], 0, target, result, candidates)
        return result


'''
40. Combination Sum II
Solved
Medium
Topics
premium lock icon
Companies
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

'''
