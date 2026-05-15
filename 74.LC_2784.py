class Solution:
    def isGood(self, nums: List[int]) -> bool:
        m = max(nums)  # maximum eleement
        if len(nums) != m +1:
            return False
        nums.sort()  # sort the arr
        arr = []  # expected arr
        for i in range(1, m+1):  # add num from 1 to m
            arr.append(i)
        arr.append(m)  # last two ele are same m, so add m.. len now m+1
        if arr == nums:  # check if both arrays are same
            return True
        return False

# good arr len must be m + 1, as last two are same i.e, m  and m
