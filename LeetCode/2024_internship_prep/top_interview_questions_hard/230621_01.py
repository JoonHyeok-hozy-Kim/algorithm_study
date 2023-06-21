class MedianFinder:

    def __init__(self):
        self._small, self._large = [], []

    def addNum(self, num: int) -> None:
        heappush(self._large, -heappushpop(self._small, -num))        
        while len(self._small) < len(self._large):
            heappush(self._small, -heappop(self._large))

    def findMedian(self) -> float:
        if (len(self._small) + len(self._large)) % 2 == 0:
            return (self._large[0] - self._small[0]) / 2
        else:
            return -self._small[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()