class Solution:
    def countAndSay(self, n: int) -> str:
        num_list = ['1']
        
        for i in range(n-1):
            temp = []
            curr = num_list[0]
            cnt = 1
            j = 1
            while j < len(num_list):
                if num_list[j] == curr:
                    cnt += 1
                else:
                    temp.append(str(cnt))
                    temp.append(str(curr))
                    curr = num_list[j]
                    cnt = 1
                j += 1
            temp.append(str(cnt))
            temp.append(str(curr))
            num_list = temp
        
        return ''.join(num_list)