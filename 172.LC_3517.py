class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0] * 26          # Frequency of each letter
        for i in s:
            freq[ord(i) - ord('a')] += 1   # Count characters
        x = []                   # Stores left half
        mid = ""                 # Stores middle character (if any)
        for i in range(26):
            x.append(chr(i + ord('a')) * (freq[i] // 2))  # Add half occurrences
            if freq[i] % 2:
                mid = chr(i + ord('a'))   # Find odd-frequency character
        x = "".join(x)           # Convert list to string
        return x + mid + x[::-1] # Left + middle + reversed left


'''
3517. Smallest Palindromic Rearrangement I
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a palindromic string s.

Return the lexicographically smallest palindromic permutation of s.

 

Example 1:

Input: s = "z"

Output: "z"

Explanation:

A string of only one character is already the lexicographically smallest palindrome.

Example 2:

Input: s = "babab"

Output: "abbba"

Explanation:

Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

Example 3:

Input: s = "daccad"

Output: "acddca"

Explanation:

Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.

 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
s is guaranteed to be palindromic.

'''
