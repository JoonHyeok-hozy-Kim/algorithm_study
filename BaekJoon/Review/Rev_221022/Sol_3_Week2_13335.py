"""
https://www.acmicpc.net/problem/13335
"""


from collections import deque


if __name__ == '__main__':
    N, W, L = map(int, input().split())
    trucks = deque(map(int, input().split()))
    # print(trucks)

    time = 0
    current_weight = 0
    bridge = deque()
    for _ in range(W):
        bridge.append(0)
    while len(trucks) > 0:
        time += 1
        current_weight -= bridge.popleft()
        if current_weight + trucks[0] <= L:
            t = trucks.popleft()
            bridge.append(t)
            current_weight += t
        else:
            bridge.append(0)
        # print(time, current_weight, bridge)

    print(time + W)