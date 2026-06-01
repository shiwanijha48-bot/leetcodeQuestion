class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sum_of_digit(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total
        res = float('inf')
        for num in nums:
            res = min(res, sum_of_digit(num))
        return res
