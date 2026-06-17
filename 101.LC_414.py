class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        setnums = set(nums)
        setnums = sorted(setnums, reverse = True) # descending order me sort then return starting se 3rd elemnt
        if len(setnums) >= 3:
            return setnums[2] # 3rd ele from start
        else:
            return setnums[0]  # maximum num
