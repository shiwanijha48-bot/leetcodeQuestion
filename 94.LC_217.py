class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


        '''setnums = set()
        for i in nums:
            if i in setnums:
                return True
            else:
                setnums.add(i)
        return False'''


        '''freq = {}
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
