class Solution:
    def minimumFlips(self, n: int) -> int:
        s = bin(n)[2:]  # convert num into bin and remove'0b'
        n = len(s) # len of bin string
        count = 0 # count num of mismatched pairs
        for i in range(0, n): # traverse all
            if s[i] != s[n-1-i]: # compare current char, with its opp char
                count += 1 # if diff , one mismatch found
        return count # return total mismatch
