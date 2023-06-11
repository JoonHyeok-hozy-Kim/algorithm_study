class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)
        dp = [gas[i] - cost[i] for i in range(N)]

        if sum(dp) < 0:
            return -1
        
        start = 0
        curr = 0
        for i, v in enumerate(dp):
            curr += v
            if curr < 0:
                start = i+1
                curr = 0
        
        return start