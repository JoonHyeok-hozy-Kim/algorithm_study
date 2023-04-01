class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        M = {}
        PQ = []
        used = deque()
        result = 0
        
        for t in tasks:
            if t not in M:
                M[t] = 1
            else:
                M[t] += 1
        
        nt = len(M)
        
        for t in M:
            heappush(PQ, [-M[t], M])
        
        for i in range(n):
            used.append(None)
        
        while nt > 0:
            if len(PQ) == 0:
                curr = None
            else:
                curr = heappop(PQ)
                if curr[0] < -1:
                    curr[0] += 1
                else:
                    curr = None
                    nt -= 1
            result += 1
            
            if n > 0:
                pop_used = used.popleft()
                if pop_used:
                    heappush(PQ, pop_used)            
                used.append(curr)
            elif curr:
                heappush(PQ, curr)
        
        return result