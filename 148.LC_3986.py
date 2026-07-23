class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        h = int(startTime[0:2])
        m = int(startTime[3:5])
        s = int(startTime[6:8])

        eh = int(endTime[0:2])
        em = int(endTime[3:5])
        es = int(endTime[6:8])
        start = h * 3600 + m * 60 + s
        end = eh * 3600 + em * 60 + es
        return end - start


'''
3986. Number of Elapsed Seconds Between Two Times
Solved
Easy
premium lock icon
Companies
Hint
You are given two valid times startTime and endTime, each represented as a string in the format "HH:MM:SS".

Return the number of seconds that have elapsed from startTime to endTime.

 

Example 1:

Input: startTime = "01:00:00", endTime = "01:00:25"

Output: 25

Explanation:

endTime is 25 seconds ahead of startTime.
Example 2:

Input: startTime = "12:34:56", endTime = "13:00:00"

Output: 1504

Explanation:

endTime is 25 minutes and 4 seconds ahead of startTime, which equals 1504 seconds.

 

Constraints:

startTime.length == 8
endTime.length == 8
startTime and endTime are valid times in the format "HH:MM:SS"
00 <= HH <= 23
00 <= MM <= 59
00 <= SS <= 59
endTime is not earlier than startTime

'''
