class Solution:
    def __init__(self):
        # Phone keypad mapping - same as traditional phone buttons
        self.digits_to_letters = {
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def helper(self, digits, ans, index, current):
        # Base case: processed all digits, we have a complete combination
        if index == len(digits):
            ans.append(current)  # Add the complete combination to results
            return

        # Get all possible letters for the current digit
        letters = self.digits_to_letters.get(digits[index], "")
        
        # Try each possible letter for this digit position
        for letter in letters:
            # Recursive call: move to next digit, extend current combination
            self.helper(digits, ans, index + 1, current + letter)

    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        # Handle edge case: empty input
        if not digits:
            return ans
        # Start the backtracking process
        self.helper(digits, ans, 0, "")  # index=0, current=""
        return ans




'''

17. Letter Combinations of a Phone Number
Solved
Medium
Topics
premium lock icon
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

1 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].


'''
