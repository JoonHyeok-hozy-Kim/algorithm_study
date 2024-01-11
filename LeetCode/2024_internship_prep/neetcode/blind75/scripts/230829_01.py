class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        curr_min = min(height[left], height[right])
        result = 0

        while left < right:
            if height[left] > height[right]:
                if height[right] < curr_min:
                    result += curr_min - height[right]
                right -= 1
            
            else:
                if height[left] < curr_min:
                    result += curr_min - height[left]
                left += 1
            
            if curr_min < min(height[left], height[right]):
                curr_min = min(height[left], height[right])
        
        return result