class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = {}  # freq of each num
        for i in nums:
            if i in freq: # if already there, inc count 
                freq[i] += 1
            else:  # first occurence
                freq[i] = 1
        ans  = 0 # storeing final ans
        for i in freq: # traversing each unique num
            if freq[i] % k == 0: # checking if its freq is div by k
                ans += i * freq[i] # add num * its freq to he ans
        return ans
