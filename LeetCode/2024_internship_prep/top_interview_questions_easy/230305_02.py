class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for i in range(numRows-1):
            temp = [1]
            for j in range(i):
                temp.append(result[-1][j] + result[-1][j+1])
            temp.append(1)
            result.append(temp)
        return result