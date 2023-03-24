class Solution:
    def searchMatrix(self, matrix: list, target: int) -> bool:
        def _edge_min(point):
            i, j = point
            return min(matrix[i][0], matrix[0][j])
        
        def _diagonal(start, end):            
            print('At _diagonal, s : {}, e : {}'.format(start, end))
            if start == end:
                return False
            mi, mj = (start[0]+end[0])//2, (start[1]+end[1])//2
            if target == matrix[mi][mj]:
                return True
            elif _edge_min([mi, mj]) <= target < matrix[mi][mj]:
                if _row([mi, mj]) or _col([mi, mj]):
                    return True
            if mi == start[0] and mj == start[1]:
                return False
            
            if target < matrix[mi][mj]:
                return _diagonal(start, [mi, mj])
            else:
                return _diagonal([mi+1, mj+1], end)
        
        def _row(point):
            print('At _row, point : {}'.format(point))
            i, j = point
            start, end = 0, j
            while start < end:
                mid = (start + end) // 2
                if target == matrix[i][mid]:
                    return True
                elif target < matrix[i][mid]:
                    end = mid
                else:
                    start = mid+1
            return False
        
        def _col(point):
            print('At _col, point : {}'.format(point))
            i, j = point
            start, end = 0, i
            while start < end:
                mid = (start + end) // 2
                if target == matrix[mid][j]:
                    return True
                elif target < matrix[mid][j]:
                    end = mid
                else:
                    start = mid+1
            return False
        
        
        e = [len(matrix), len(matrix[0])]
        min_len = min(e)
        s = [e[0]-min_len, e[1]-min_len]
        return _diagonal(s, e)


if __name__ == '__main__':
    s = Solution()
    a = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
    print(s.searchMatrix(a, 5))
