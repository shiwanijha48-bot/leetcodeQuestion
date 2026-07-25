class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        res = []
        for n in range(2, 10):  
            for i in range(0, 10-n):
                num = int(s[i : i +n])
                if low <= num <= high:
                    res.append(num)
        return res

        # sequential number must be of 2 digit, ek jada hoga uska dusra dgit like 12, 23, 34, etc.. range(2, 10)
        # (0, 10-n) if n = 3 we want substring of length = 3. so we start from 1 to 7. as last number will be 789(123,234,345,456,567,678,789). so i should go from 0 to 6 index i.e, 1 to 7.
        # s[i : i+n] = s[start:end]= takes characs from start to end - 1... s[2:6] = "3456"

'''
1291. Sequential Digits
Solved
Medium
Topics
premium lock icon
Companies
Hint
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
'''
