from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self._left = []
        self._right = []
        self._n = 0

    def addNum(self, num: int) -> None:
        if len(self._left) == 0 or -self._left[0] > num:
            heappush(self._left, -num)
        else:
            heappush(self._right, num)

        while len(self._left) - len(self._right) > 1:
            a = heappop(self._left)
            heappush(self._right, -a)
        while len(self._left) < len(self._right):
            a = heappop(self._right)
            heappush(self._left, -a)
        # print(self._left, self._right)

    def findMedian(self) -> float:
        L = len(self._left) + len(self._right)
        if L % 2 == 0:
            return (self._right[0] - self._left[0]) / 2
        else:
            return -self._left[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()