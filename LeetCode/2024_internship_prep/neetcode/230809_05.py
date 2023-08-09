class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        Q = []
        result = []

        for n in nums:
            freq[n] += 1
        
        for f in freq.keys():
            heappush(Q, (-freq[f], f))
        
        for _ in range(k):
            result.append(heappop(Q)[1])
        
        return result