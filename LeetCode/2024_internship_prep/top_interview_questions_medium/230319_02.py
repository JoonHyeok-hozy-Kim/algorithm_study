class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        Q = deque()
        Q.append([])
        for i, v in enumerate(nums):
            new_q = deque()
            while Q:
                popped = Q.popleft()
                copied = deepcopy(popped)
                copied.append(v)
                new_q.append(popped)
                new_q.append(copied)
            Q = new_q
        
        return Q