"""
13335. 트럭
https://www.acmicpc.net/problem/13335
"""
from collections import deque

if __name__ == '__main__':
    N, W, L = map(int, input().split())
    trucks = deque(map(int, input().split()))
    bridge = deque()
    current_weight = 0
    time_cnt = 0
    for _ in range(W):
        bridge.append(0)
    # print(bridge)
    while len(trucks) > 0:
        time_cnt += 1
        current_weight -= bridge.popleft()
        if current_weight + trucks[0] <= L:
            new_truck = trucks.popleft()
            current_weight += new_truck
            bridge.append(new_truck)
        else:
            bridge.append(0)
        # print(bridge)
    time_cnt += W
    print(time_cnt)
