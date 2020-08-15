"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
"""
def eraseOverlapIntervals(intervals):
    result = 0
    if len(intervals) < 2:
        return 0
    intervals.sort(key=lambda x:x[0])
    current_min = intervals[0][1]
    for i in intervals:
        if current_min > i[0]:
            result+=1
            current_min = min(current_min, i[1]) #if they overlap, erase the one with bigger interval
        else:
            current_min = max(current_min, i[1]) 
    return result-1 #minus 1 because we don't count the first interval being overlapped
            