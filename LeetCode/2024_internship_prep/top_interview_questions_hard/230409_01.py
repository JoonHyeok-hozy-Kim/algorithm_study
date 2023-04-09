class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''Set Sol.'''
        S = set(nums)
        result = 0
        for n in S:
            if n-1 not in S:
                l = 1
                while n+l in S:
                    l += 1
                result = max(result, l)
        return result
        
        '''Hash Map Sol.'''
#         M = {}
#         result = 0
        
#         for i, v in enumerate(nums):
#             M[v] = True
        
#         for i, v in enumerate(nums):
#             if v-1 in M:
#                 M[v] = False
        
#         for i, v in enumerate(nums):
#             if M[v]:
#                 j = cnt = 1
#                 while v+j in M and not M[v+j]:
#                     j += 1
#                     cnt += 1
#                 result = max(result, cnt)
        
#         return result