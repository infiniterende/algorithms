import heapq


def merge_intervals(intervals):
    heap = []
    res = []
    heapq.heappush(heap, intervals[0])

    for i in range(1, len(intervals)):
        if heap[0][1] >= intervals[i][0]:
            popped = heapq.heappop(heap)
            newInterval = [min(popped[0], intervals[i][0]),
                           max(popped[1], intervals[i][1])]
            heapq.heappush(heap, newInterval)
        else:
            popped = heapq.heappop(heap)
            res.append(popped)
            heapq.heappush(heap, intervals[i])
    res.append(heapq.heappop(heap))
    return res
