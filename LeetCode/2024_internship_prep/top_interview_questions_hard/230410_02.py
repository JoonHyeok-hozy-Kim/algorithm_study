class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        Q = deque()
        Q.append((nums[0], 0))
        for i in range(1, k):
            while Q and Q[-1][0] <= nums[i]:
                Q.pop()
            Q.append((nums[i], i))
        
        result.append(Q[0][0])
        for j in range(k, len(nums)):
            while Q and Q[0][1] <= j-k:
                Q.popleft()
            
            while Q and Q[-1][0] <= nums[j]:
                Q.pop()
            
            Q.append((nums[j], j))
            result.append(Q[0][0])
        
        return result