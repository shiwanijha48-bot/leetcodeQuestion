class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        res = []
        freq = {}
        ans = 0
        for i in s:
            res.append(i)
            freq[i] = freq.get(i,0)+1
            while freq[i] > 2:
                x = res.pop(0)
                freq[x] -= 1
            ans = max(ans, len(res))
        return ans



'''
3090. Maximum Length Substring With Two Occurrences
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:

The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
Example 2:

Input: s = "aaaa"

Output: 2

Explanation:

The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

Constraints:

2 <= s.length <= 100
s consists only of lowercase English letters.
'''
