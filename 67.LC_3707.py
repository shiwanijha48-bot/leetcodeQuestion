class Solution:
    def scoreBalance(self, s: str) -> bool:
        total = 0
        for ch in s:
            total += ord(ch) - ord('a') + 1 # total score of str
        leftsum  = 0 
        for i in range(0, len(s) - 1): # iterate till second last (so right part not empty)
            leftsum += ord(s[i]) - ord('a') + 1 # add curr chr val to left
            if leftsum == total - leftsum: # rem sum is right, valid if both equal
                return True   # if equal split found
        return False   # no valid split exists

#  Main intuition =  converting string ka character to ascii value then as we need a = 1, b = 2, c = 3.... 
# so subtrating the a ki asccii value from eveery character to get the values like that.
#  (ord(c) - ord('a') + 1) = ord of c = 99 - ord of a = 97 so, 99-97= 2 but c should be equal to 3. 
# so adding 1.. then c = 99 - 97 + 1 = 3... 
