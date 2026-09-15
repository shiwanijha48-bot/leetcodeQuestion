class Solution:
    def removeZeros(self, n: int) -> int:
        s = str(n).replace("0", "")
        return int(s)


'''
3726. Remove Zeros in Decimal Representation
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a positive integer n.

Return the integer obtained by removing all zeros from the decimal representation of n.

 

Example 1:

Input: n = 1020030

Output: 123

Explanation:

After removing all zeros from 1020030, we get 123.

Example 2:

Input: n = 1

Output: 1

Explanation:

1 has no zero in its decimal representation. Therefore, the answer is 1.

 

Constraints:

1 <= n <= 1015
'''
