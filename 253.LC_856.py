class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for ch in s:
            if ch == '(':  # Start a new level
                stack.append(0)
            else: # Get the score inside the current ()
                inside = stack.pop()  # "()" = 1, otherwise "(A)" = 2 * A
                score = max(2 * inside, 1)  # Add score to the previous level
                stack[-1] += score
        return stack[0]


'''
856. Score of Parentheses
Solved
Medium
Topics
premium lock icon
Companies
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: s = "()"
Output: 1
Example 2:

Input: s = "(())"
Output: 2
Example 3:

Input: s = "()()"
Output: 2
 

Constraints:

2 <= s.length <= 50
s consists of only '(' and ')'.
s is a balanced parentheses string.
'''
