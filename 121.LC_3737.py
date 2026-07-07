class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = 0 # count of valid sbarrays
        n = len(nums) # lenb of arra
        for i in range(0, n): # start subarr from each ind
            s = 0 # balance count, target = +1, others = -1
            for j in range(i, n): #extend subarr till end
                if nums[j] == target: #
                    s += 1 # inc if target found
                else: 
                    s -= 1 # dec if not found
                if s > 0: # target appears more than half
                    res += 1 # valid subarray
        return res
