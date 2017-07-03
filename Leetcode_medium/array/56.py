# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        if intervals == []:
            return []
        intervals.sort(key=lambda x:(x.start, x.end))
        for i, v in enumerate(intervals):
            if i == 0:
                res.append(v)
            else:
                w = res[-1]
                if w.end >= v.start:
                    if w.end < v.end:
                        w.end = v.end
                else:
                    res.append(v)
        return res


s = Solution()
x = []
lst = [[1,3],[2,6],[8,10],[15,18]]
for i in lst:
    x.append(Interval(i[0], i[1]))
    print(x[-1].start, x[-1].end)
s.merge(x)
