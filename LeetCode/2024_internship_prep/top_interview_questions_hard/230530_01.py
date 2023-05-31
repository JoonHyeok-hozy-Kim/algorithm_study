class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        freq = [0 for _ in range(5001)]
        
        for n in nums:
            freq[n] += 1
        
        '''
        _ _ _ _   (N=4, Med = 1) -> Med = N//2 - 1
        _ _ _ _ _ (N=5, Med = 2) -> Med = N//2        
        
        '''
        curr_idx = -1
        median_idx = N//2 - 1 if N%2 == 0 else N//2
        curr_val = 0

        print('median_idx : {}'.format(median_idx))

        while curr_idx < median_idx:
            while freq[curr_val] == 0:
                curr_val += 1
            if curr_idx + freq[curr_val] >= median_idx:
                median_val = curr_val
                break
            else:
                curr_idx += freq[curr_val]
                curr_val += 1
        
        split_for_left = median_idx - curr_idx
        split_for_right = freq[median_val] - split_for_left

        print('median_idx : {}, split_for_left : {}, split_for_right : {}'.format(median_idx, split_for_left, split_for_right))
        
        even = 0
        odd = N-1 if N%2 == 0 else N-2
        for i in range(split_for_left):
            nums[even] = median_val
            even += 2
        for i in range(split_for_right):
            nums[odd] = median_val
            odd -= 2
        
        left_val = median_val - 1
        right_val = median_val + 1
        
        while even < N:
            while freq[left_val] == 0:
                left_val -= 1
            nums[even] = left_val
            freq[left_val] -= 1
            even += 2
        
        while odd >= 0:
            while freq[right_val] == 0:
                right_val += 1
            nums[odd] = right_val
            freq[right_val] -= 1
            odd -= 2

if __name__ == '__main__':
    S = Solution()
    l = [1,3,2,2,3,1]
    S.wiggleSort(l)
    print(l)