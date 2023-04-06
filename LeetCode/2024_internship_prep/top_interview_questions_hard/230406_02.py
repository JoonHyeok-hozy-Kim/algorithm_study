class Solution:
    def maxArea(self, height: List[int]) -> int:
        # O(N) sol
        left, right = 0, len(height)-1
        result = 0
        while left < right:
            curr_area = (right - left) * min(height[left], height[right])
            result = max(result, curr_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return result
        
        # O(N log(N)) sol.
#         result = 0
#         height_sorted = [(h, i) for i, h in enumerate(height)]
#         height_sorted.sort(reverse=True)
#         min_k = height_sorted[0][1]
#         max_k = height_sorted[0][1]
#         for i in range(1, len(height_sorted)):
#             if height_sorted[i][1] < min_k:
#                 min_k = height_sorted[i][1]
#             elif height_sorted[i][1] > max_k:
#                 max_k = height_sorted[i][1]
            
#             width = max(max_k - height_sorted[i][1], height_sorted[i][1] - min_k)
#             result = max(result, height_sorted[i][0] * width)
        
#         return result