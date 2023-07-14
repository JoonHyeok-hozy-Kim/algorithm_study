class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        M = defaultdict(int)
        H = []
        reverse = True if k > len(nums) // 2 else False
        if reverse:
            k = len(nums) - k + 1
        
        for n in nums:
            M[n] += 1
            if M[n] == 1:
                if reverse:
                    n *= -1
                heappush(H, -n)
        
        cnt = 0
        while cnt < k:
            x = heappop(H)
            if reverse:
                x *= -1
            cnt += M[-x]
        
        return -x