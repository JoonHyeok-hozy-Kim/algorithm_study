class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        result = 0
        while left < right:
            temp = (right - left) * min(height[left], height[right])
            result = max(result, temp)

            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        
        return result