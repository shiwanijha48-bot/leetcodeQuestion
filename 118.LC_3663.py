class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        freq = {}  # store frequency of each digit
        for i in str(n): # convert number to string to access digits
            if i in freq:
                freq[i] += 1  # increase count if digit already exists
            else:
                freq[i] = 1  # first occurrence of digit
        mini = min(freq.values())  # find minimum frequency
        res = []
        for i in freq: # check all digits
            if freq[i] == mini:
                res.append(int(i)) # store digits with least frequency
        return min(res)   # return smallest digit among them
