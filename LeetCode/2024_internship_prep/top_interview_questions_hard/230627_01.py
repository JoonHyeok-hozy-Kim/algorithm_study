class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        s_pointer = s_peak = 0
        e_pointer = e_peak = N-1
        result = 0
        
        def calculate_amount_of_water(p1, p2):
            amount = 0
            min_peak_height = min(height[p1], height[p2])
            
            if p1 < p2:
                for i in range(p1+1, p2):
                    amount += min_peak_height - height[i]
            
            return amount
        
        while s_peak < e_peak:
            if s_pointer < N and height[s_peak] < height[s_pointer]:
                result += calculate_amount_of_water(s_peak, s_pointer)
                s_peak = s_pointer
            
            if e_pointer >= 0 and height[e_peak] < height[e_pointer]:
                result += calculate_amount_of_water(e_pointer, e_peak)
                e_peak = e_pointer
            
            if s_pointer < N:            
                s_pointer += 1
            if e_pointer >= 0:
                e_pointer -= 1
            
            if s_pointer == N and e_pointer == -1:
                break
        
        return result + calculate_amount_of_water(s_peak, e_peak)