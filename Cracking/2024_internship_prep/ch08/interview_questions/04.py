from collections import deque
from copy import deepcopy

def power_set(S):
    Q = deque()
    Q.append([])
    for i in S:
        temp = deque()
        while Q:
            popped = Q.popleft()
            new = deepcopy(popped)
            new.append(i)
            temp.append(popped)
            temp.append(new)
        Q = temp
    return list(Q)


if __name__ == '__main__':
    s = [1,2,3,4]
    print(power_set(s))
