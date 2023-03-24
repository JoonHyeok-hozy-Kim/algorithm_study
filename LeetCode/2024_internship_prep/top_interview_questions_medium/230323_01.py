class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        
        while l < r:
            m = (l+r) // 2
            if nums[m] == target:
                return m
            elif m == l:
                return -1
            
            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m+1            
            else:
                if nums[m] < target <= nums[r-1]:
                    l = m+1
                else:
                    r = m
            
        return -1
        
#         def _recursive(N, t, left, right):            
#             mid = (left + right) // 2
#             if mid == left and N[mid] != t:
#                 return -1
            
#             if N[left] < N[mid]:
#                 if N[left] <= t <= N[mid-1]:
#                     return _binary_search(N, t, left, mid)
#                 else:
#                     return _recursive(N, t, mid, right)
#             else:
#                 if N[mid] <= t <= N[right-1]:
#                     return _binary_search(N, t, mid, right)
#                 else:
#                     return _recursive(N, t, left, mid)
        
#         def _binary_search(N, t, left, right):
#             mid = (left + right) // 2
#             if mid == left and N[mid] != t:
#                 return -1
            
#             if N[mid] == t:
#                 return mid
#             elif N[mid] > t:
#                 return _binary_search(N, t, left, mid)
#             else:
#                 return _binary_search(N, t, mid, right)
        
#         return _recursive(nums, target, 0, len(nums))