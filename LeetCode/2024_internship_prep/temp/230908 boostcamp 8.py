import sys
sys.setrecursionlimit(10000) 

def solution(n, s):
    from copy import deepcopy
    record = {}
    
    def _recursive(rn, rs):
        
        if (rn, rs) in record:
            return record[(rn, rs)]
        
        elif rn == 1:
            record[(rn, rs)] = [rs, [rs]]
            
        elif rn > rs:
            record[(rn, rs)] = [-1, [-1]]
        
        else:
            curr_val = 0
            curr_arr = []
            
            for i in range(1, rs-(rn-1)):
                prev_val, prev_arr = _recursive(rn-1, rs-i)
                if prev_val == -1:
                    curr_val = -1
                    curr_arr = [-1]
                    continue

                temp_val = i * prev_val
                if curr_val < temp_val:
                    curr_val = temp_val
                    curr_arr = deepcopy(prev_arr)
                    curr_arr.append(i)
                    curr_arr.sort()
                    
            record[(rn, rs)] = [curr_val, curr_arr]
        
        print('_recursive({}, {}), len(record)={}, {}'.format(rn, rs, len(record), record[(rn, rs)][1]))
        return record[(rn, rs)]
    
    V, A = _recursive(n, s)
    # print(record)
    return A


if __name__ == '__main__':
    print(solution(100, 10000))