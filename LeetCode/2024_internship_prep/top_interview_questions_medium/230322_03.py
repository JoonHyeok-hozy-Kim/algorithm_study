class Solution:
    def merge(self, intervals: list) -> list:
        return self._recursive(intervals)
        
    def _recursive(self, S, depth=0):
        for i in range(depth):
            print("  ", end="")
        print('At _recursive : {}'.format(S))
        if len(S) <= 1:
            return S

        mid = len(S)//2
        s1 = self._recursive(S[:mid], depth+1)
        s2 = self._recursive(S[mid:], depth+1)
        result = self._merge_lists(s1, s2)
        for i in range(depth):
            print("  ", end="")
        print(result)
        return result

    def _merge_lists(self, s1, s2):
        print('At _merge_lists, s1 : {}, s2 : {}'.format(s1, s2))
        i1 = i2 = 0
        result = []
        temp = None
        while i1 < len(s1) or i2 < len(s2):
            print('temp : {}, i1 : {}, i2 : {}'.format(temp, i1, i2))
            if i1 == len(s1):
                if temp is None:
                    result.extend(s2[i2:])
                    break
                else:
                    if self._overlaps(temp, s2[i2]):
                        temp = self._merge_intervals(temp, s2[i2])
                        i2 += 1
                    else:
                        result.append(temp)
                        temp = None
            elif i2 == len(s2):
                if temp is None:
                    result.extend(s1[i1:])
                    break
                else:
                    if self._overlaps(temp, s1[i1]):
                        temp = self._merge_intervals(temp, s1[i1])
                        i1 += 1
                    else:
                        result.append(temp)
                        temp = None
            else:
                if temp is None:
                    if self._overlaps(s1[i1], s2[i2]):
                        temp = self._merge_intervals(s1[i1], s2[i2])
                        i1 += 1
                        i2 += 1
                    else:
                        if s1[i1][0] < s2[i2][0]:
                            result.append(s1[i1])
                            i1 += 1
                        else:
                            result.append(s2[i2])
                            i2 += 1
                else:
                    if self._overlaps(temp, s1[i1]):
                        temp = self._merge_intervals(temp, s1[i1])
                        i1 += 1
                    elif self._overlaps(temp, s2[i2]):
                        temp = self._merge_intervals(temp, s2[i2])
                        i2 += 1
                    else:
                        result.append(temp)
                        temp = None

        if temp is not None:
            result.append(temp)                    

        return result

    def _overlaps(self, intv1, intv2):
        if len(intv1) == 0 or len(intv2) == 0:
            return False
        if max(intv1[0], intv2[0]) <= min(intv1[1], intv2[1]):
            return True
        return False

    def _merge_intervals(self, intv1, intv2):
        return [min(intv1[0], intv2[0]), max(intv1[1], intv2[1])]
        
if __name__ == '__main__':
    i = [[1,4],[0,2],[3,5]]
    s = Solution()
    s.merge(i)