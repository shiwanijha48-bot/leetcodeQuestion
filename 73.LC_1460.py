class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort() # sort target arr
        arr.sort()   # sort arr 
        if target == arr:  # if both same, then true
            return True
        else:
            return False
-------------------------------------------------------------------------
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        freq = {}  # freq to store target ele
        for i in target: # count each no. in target
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        for i in arr:  # decreasing count using arr ele
            if i not in freq:  # ele not found
                return False
            freq[i] -= 1    # found, dec count
            if freq[i] < 0:   # extra occurence found
                return False
        return True   # both arrs have same freq
