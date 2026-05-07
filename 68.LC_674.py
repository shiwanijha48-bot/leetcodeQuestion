class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:   # if list is empty
            return 0
        maxLen = 1    # stores max length
        currLen = 1   # stores current increasing length
        for i in range(1, len(nums)):   # itearate array from ind
            if nums[i] > nums[i-1]:     # if inc seq continues
                currLen += 1
            else:       # seq break
                currLen = 1
            maxLen = max(maxLen, currLen)     # update max length
        return maxLen   # final ans  
