from typing import List 

class Interval:
    def __init__(self, start, end) -> None:
        self.start = start 
        self.end = end

def merge(intervals: List[Interval]):
    if len(intervals)< 2:
        return 
    
    intervals.sort(key=lambda x: x.start)
    mergedIntervals = [] 
    start = intervals[0].start 
    end =  intervals[0].end
    for i in range(1, len(intervals)):
        nextInterval = intervals[i]
        if end >= nextInterval.start:
            end = max(end, nextInterval.end)
        else:
            mergedIntervals.append(Interval(start, end))
            start = nextInterval.start
            end = nextInterval.end
    mergedIntervals.append(Interval(start, end)) 
    return mergedIntervals

def mergeExclusive(intervals: List[Interval], insertPoint: Interval):
    intervals.append(insertPoint)
    
    intervals.sort(key=lambda x: x.start)
    mergedIntervals = [] 
    start = intervals[0].start 
    end =  intervals[0].end
    for i in range(1, len(intervals)):
        nextInterval = intervals[i]
        if end >= nextInterval.start:
            # this means that we have an overlapping interval
            end = max(end, nextInterval.end)
            mergedIntervals.append(Interval(start, end))
        else:
            # mergedIntervals.append(Interval(start, end))
            start = nextInterval.start
            end = nextInterval.end
    # mergedIntervals.append(Interval(start, end)) 
    return mergedIntervals

merge(
    intervals= [Interval(3,7),Interval(1,2), Interval(5,6)]
)

mergeExclusive(
    intervals= [Interval(3,7),Interval(1,2), Interval(11,13)],
    insertPoint=Interval(2,6)
)