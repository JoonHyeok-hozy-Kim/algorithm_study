def height_of_stack(boxes):
    M = {}
    for i, bi in enumerate(boxes):
        for j, bj in enumerate(boxes):
            if bi[0] > bj[0] and bi[1] > bj[1] and bi[2] > bj[2]:
                if j not in M:
                    M[j] = [i]
                else:
                    M[j].append(i)
    
    result = 0
    for i in M:
        result = max(result, dfs(M, i))
    return result

def dfs(M, i):
    result = 1
    if i in M:
        for j in M[i]:
            result = max(result, dfs(M, j) + 1)
    return result


if __name__ == '__main__':
    b = [
        [1,2,3],
        [2,3,4],
        [3,4,5],
        [3,4,4],
        [10,3,4],
        [11,4,5],
        [12,5,7],
    ]
    print(height_of_stack(b))
