class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        cnt = Counter(nums)
        result_set = set()

        if 0 in cnt:
            if cnt[0] >= 3:
                result_set.add((0,0,0))
        
            for k in cnt.keys():
                if k > 0 and -k in cnt:
                    temp = (-k, 0, k)
                    result_set.add(temp)
        
        keys = list(cnt.keys())
        for i in range(len(keys)):
            if keys[i] == 0:
                continue
            for j in range(i+1, len(keys)):
                if keys[j] == 0:
                    continue
                x = -(keys[i] + keys[j])
                if x in cnt:
                    if x == keys[i] and cnt[x] == 1:
                        continue
                    if x == keys[j] and cnt[x] == 1:
                        continue

                    temp = [keys[i], keys[j], -(keys[i] + keys[j])]
                    temp.sort()
                    tt = tuple(temp)
                    # print(tt)
                    result_set.add(tt)
        
        return list(result_set)