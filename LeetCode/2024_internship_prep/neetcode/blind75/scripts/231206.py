class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l < r:
            if target == nums[l]:
                return l
            elif target == nums[r]:
                return r

            if nums[l] < nums[r]:
                if target < nums[l] or target > nums[r]:
                    return -1
                    
                m = (l+r) // 2
                if l == m:
                    break
                if target == nums[m]:
                    return m
                elif target < nums[m]:
                    r = m
                else:
                    l = m
            else:
                m = (l+r) // 2
                if l == m:
                    break
                if target == nums[m]:
                    return m
                if nums[m] > nums[l]:
                    if target > nums[m]:
                        l = m
                    else:
                        if target > nums[l]:
                            r = m
                        elif target < nums[r]:
                            l = m
                        else:
                            return -1
                else:
                    if target < nums[m]:
                        r = m
                    else:
                        if target > nums[l]:
                            r = m
                        elif target < nums[r]:
                            l = m
                        else:
                            return -1
        
        if nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        return -1