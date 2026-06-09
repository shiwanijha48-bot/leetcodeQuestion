class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))      # Method 1


        '''setnums = set()           # Method 2
        for i in nums:
            if i in setnums:
                return True
            else:
                setnums.add(i)
        return False'''


        '''freq = {}           # Method 3
        for i in nums:
            freq[i] = freq.get(i,0) + 1
            # if i in freq:
            #     freq[i] += 1
            # else:
            #     freq[i] = 1
            if freq[i] == 2:
                return True
        else: 
            return False'''
