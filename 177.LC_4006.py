class Solution:
    def countValidPrefixes(self, s: str) -> int:
        z = 0
        o = 0
        res = 0
        for i in s:
            if i == '0':
                z += 1
            else:
                o += 1
            if abs(z - o) <= 1:
                res += 1
        return res

  '''
4006. Count Valid Prefixes
Solved
Easy
premium lock icon
Companies
Hint
You are given a binary string s.

A prefix of s is considered valid if its characters can be rearranged to form an alternating string.

Return the number of valid prefixes of s.

A string is considered alternating if no two adjacent characters are equal.

 

Example 1:

Input: s = "00101"

Output: 3

Explanation:

The valid prefixes are:

"0": It is already an alternating string.
"001": It can be rearranged into "010", which is an alternating string.
"00101": It can be rearranged into "01010", which is an alternating string.
Thus, the answer is 3.

Example 2:

Input: s = "101"

Output: 3

Explanation:

All prefixes of s = "101" are already alternating strings. Thus, the answer is 3.

 

Constraints:

1 <= s.length <= 100
s consists only of '0' and '1'.

  '''
