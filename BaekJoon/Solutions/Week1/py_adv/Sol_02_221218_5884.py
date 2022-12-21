'''
감시 카메라
https://www.acmicpc.net/problem/5884
'''

def dfs(herd, i, x_flag, depth=0, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(i)



if __name__ == '__main__':
    N = int(input())
    herd = [None] * N
    for i in range(N):
        herd[i] = list(map(int, input().split()))
    
    print(herd)

    visited = set()
    x_map = {}
    y_map = {}

    for i in range(N):
        if herd[i][0] not in x_map:
            x_map[herd[i][0]] = []
        x_map[herd[i][0]].append(herd[i][1])

        if herd[i][1] not in y_map:
            y_map[herd[i][1]] = []
        y_map[herd[i][1]].append(herd[i][0])
    
    print(x_map)
    print(y_map)