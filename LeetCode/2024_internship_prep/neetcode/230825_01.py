class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        starts = {}
        ends = {}
        elements = []
        used = set()

        for n in nums:
            if n in used:
                continue
            
            used.add(n)
            called = False
            if n+1 in starts:
                called = True
                old = starts[n+1]
                del starts[n+1]
                old[0] = n
                starts[n] = old
            
            if n-1 in ends:
                called = True
                old = ends[n-1]
                del ends[n-1]
                old[1] = n
                ends[n] = old
            
            if called:
                if n in starts and n in ends:
                    ss, ee = ends[n][0], starts[n][1]
                    new = [ss, ee]
                    elements.append(new)
                    del ends[n]
                    del starts[n]
                    starts[ss] = new
                    ends[ee] = new
            else:
                new_element = [n, n]
                elements.append(new_element)
                starts[n] = new_element
                ends[n] = new_element
        
        result = 0
        for x in elements:
            result = max(result, x[1]-x[0]+1)
        
        return result