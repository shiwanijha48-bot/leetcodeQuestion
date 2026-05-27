class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        ans = []
        for num in nums:
            if ans.count(num) < k:
                ans.append(num)
        return ans
