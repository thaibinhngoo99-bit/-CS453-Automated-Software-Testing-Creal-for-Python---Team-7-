'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

 

Constraints:

intervals[i][0] <= intervals[i][1]
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x: x[0])
        output = []
        i = 0
        if len(intervals) <= 1:
            return intervals
        while i < len(intervals) - 1:
            tmp = intervals[i]
            while tmp[1] >= intervals[i + 1][0]:
                tmp[1] = max(tmp[1], intervals[i + 1][1])
                i += 1
                if i >= len(intervals) - 1:
                    break
            i += 1
            output.append(tmp)
        if i <= len(intervals) - 1:
            output.append(intervals[-1])
        return output
