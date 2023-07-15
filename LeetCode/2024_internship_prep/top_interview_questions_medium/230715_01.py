class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        idx = 0
        while idx < len(intervals)-1:            
            v1, v2 = intervals[idx], intervals[idx+1]
            if v1[1] >= v2[0]:
                intervals[idx+1] = [min(v1[0], v2[0]), max(v1[1], v2[1])]
                intervals.pop(idx)
            else:
                idx += 1
        
        return intervals