"""
10975. 데크 소트 2
https://www.acmicpc.net/problem/10975
"""
from copy import deepcopy
from collections import deque


def recursive_method():
    N = int(input())
    total_deque = deque()
    total_deque.append(deque())

    for _ in range(N):
        total_deque = run_recursive(total_deque, int(input()))

    result = N
    for ds in total_deque:
        # if len(ds) <= result:
        #     print(ds)
        result = min(result, len(ds))
    print(result)



def run_recursive(total_deque, new_item):
    new_total_deque = deque()
    while len(total_deque) > 0:
        temp_total_deque = add_item(total_deque.pop(), new_item)
        while len(temp_total_deque) > 0:
            new_total_deque.append(temp_total_deque.pop())

    return new_total_deque


def add_item(deque_set, new_item):
    deque_set_list = deque()

    if deque_set_validation_int(deque_set, new_item):
        new_deque = deque()
        new_deque.append(new_item)
        new_deque_set = deepcopy(deque_set)
        new_deque_set.append(new_deque)
        deque_set_list.append(new_deque_set)

    if len(deque_set) > 0:
        for _ in range(len(deque_set)):
            d = deque_set.popleft()
            if new_item < d[0]:
                d.appendleft(new_item)
                if deque_set_validation(deque_set, d):
                    new_deque = deepcopy(d)
                    new_deque_set = deepcopy(deque_set)
                    new_deque_set.append(new_deque)
                    deque_set_list.append(new_deque_set)
                d.popleft()
            elif new_item > d[-1]:
                d.append(new_item)
                if deque_set_validation(deque_set, d):
                    new_deque = deepcopy(d)
                    new_deque_set = deepcopy(deque_set)
                    new_deque_set.append(new_deque)
                    deque_set_list.append(new_deque_set)
                d.pop()
            deque_set.append(d)

    return deque_set_list


def deque_set_validation_int(deque_set, num):
    for deque in deque_set:
        if deque[0] < num and deque[-1] < num:
            None
        elif deque[0] > num and deque[-1] > num:
            None
        else:
            return False
    return True


def deque_set_validation(deque_set, new_deque):
    for deque in deque_set:
        if deque[0] < new_deque[0] and deque[-1] < new_deque[0]:
            None
        elif deque[0] > new_deque[-1] and deque[-1] > new_deque[-1]:
            None
        else:
            return False
    return True



if __name__ == '__main__':
    # recursive_method()

    N = int(input())
    l = []
    for i in range(N):
        l.append((int(input()), i))
    # print(l)
    l.sort()
    # print(l)

    cnt = 1
    up_flag = False
    for i in range(N-1):
        if up_flag:
            if l[i][1] > l[i+1][1]:
                cnt += 1
                up_flag = False
        else:
            if l[i][1] < l[i+1][1]:
                up_flag = True

    print(cnt)
