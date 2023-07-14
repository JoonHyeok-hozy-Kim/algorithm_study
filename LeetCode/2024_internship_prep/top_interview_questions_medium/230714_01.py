class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s, e = 0, len(nums)-1
        modified = True
        
        while s <= e and modified:
            modified = False
            sp = s
            while sp < e:
                while s <= e and nums[s] == 0:
                    s += 1
                    sp = s
                    modified = True
                if sp+1 <= e and nums[sp] > nums[sp+1]:
                    nums[sp], nums[sp+1] = nums[sp+1], nums[sp]
                    modified = True
                sp += 1
            
            ep = e
            while ep > s:
                while s <= e and nums[e] == 2:
                    e -= 1
                    ep = e
                    modified = True
                if s <= ep-1 and nums[ep-1] > nums[ep]:
                    nums[ep-1], nums[ep] = nums[ep], nums[ep-1]
                    modified = True
                ep -= 1