class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        prev = None
        final = []

        for i in range(len(intervals)):
            if not prev:
                prev = intervals[i]
            else:
                if prev[-1]>=intervals[i][0]:
                    prev = [min(prev[0],intervals[i][0]) , max(prev[-1], intervals[i][-1])]
                else:
                    final.append(prev)
                    prev = intervals[i]
        if prev:
            final.append(prev)
        return final

