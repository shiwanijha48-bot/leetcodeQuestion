class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        freq = {}
        for i in range(n):
            if nums[i] not in freq:
                freq[nums[i]] = []
            freq[nums[i]].append(i)
        for i in freq:
            x = freq[i]
            if len(x) >= 3:
                a = x[1] - x[0] # distance btw
                flag = True # intially i is special flag = true
                for j in range(2, len(x)):
                    if x[j] - x[j-1] != a:
                        flag = False
                        break
                if flag:
                    res += 1
        return res


'''
4049. Count Values With Equally Spaced Occurrences II
Solved
Medium
premium lock icon
Companies
Hint
You are given an integer array nums.

An integer x is called special if:

x appears at least three times in nums.
All occurrences of x are equally spaced in nums. In other words, if all occurrences of x are at indices i1 < i2 < ... < im, then i2 - i1 = i3 - i2 = ... = im - im-1.
Return the number of distinct special integers in nums.

 

Example 1:

Input: nums = [1,8,1,5,1,5,8,5]

Output: 2

Explanation:

1 is special because it occurs at equally spaced indices 0, 2, and 4.
5 is special because it occurs at equally spaced indices 3, 5, and 7.
8 is not special because it occurs only twice.
Therefore, the answer is 2.

Example 2:

Input: nums = [8,8,8,8]

Output: 1

Explanation:

8 is special because it occurs at equally spaced indices 0, 1, 2, and 3. Therefore, the answer is 1.

Example 3:

Input: nums = [8,6,6,8,8]

Output: 0

Explanation:

8 occurs at indices 0, 3, and 4, which are not equally spaced. 6 occurs only twice. Therefore, no integer is special.

 

Constraints:

3 <= nums.length <= 105
1 <= nums[i] <= 109
 

'''
