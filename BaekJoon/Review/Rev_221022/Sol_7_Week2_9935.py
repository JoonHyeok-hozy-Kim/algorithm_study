"""
https://www.acmicpc.net/problem/9935
"""


def list_solution():
    target_text = list(input())
    explosive = input()
    # print(target_text, explosive)

    idx = 0
    while idx < len(target_text):
        identical = 0
        explosion_flag = False
        while idx+identical < len(target_text) and target_text[idx+identical] == explosive[identical]:
            # print('{} vs {}'.format(target_text[idx+identical], explosive[identical]))
            identical += 1
            if identical == len(explosive):
                # print('EXPLOSION at {}'.format(idx))
                explosion_flag = True
                break

        if explosion_flag:
            temp_target = target_text[:idx]
            temp_target.extend(target_text[idx+len(explosive):])
            # for _ in range(len(explosive)):
            #     target_text.pop(idx)
            target_text = temp_target
            idx = max(0, idx-len(explosive))
        else:
            idx += 1

        # print(target_text)

    if len(target_text) == 0:
        print('FRULA')
    else:
        print(''.join(target_text))


from collections import deque

def deque_solution():
    target_text = deque(input())
    explosive = input()
    # print(target_text, explosive)

    used = []
    while len(target_text) > 0:
        identical = 0
        while identical < len(target_text) and identical < len(explosive) and target_text[identical] == explosive[identical]:
            # print('{} vs {}'.format(target_text[identical], explosive[identical]))
            identical += 1

        if identical == len(explosive):
            for _ in range(identical):
                target_text.popleft()
            while len(used) > 0 and identical > 1:
                if used[-1] not in explosive:
                    break
                target_text.appendleft(used.pop())
                identical -= 1

        elif identical > 0:
            for j in range(identical):
                if len(target_text) > 0:
                    used.append(target_text.popleft())

        elif len(target_text) > 0:
            used.append(target_text.popleft())

        # print(used, target_text)

    if len(used) > 0:
        print(''.join(used))
    else:
        print('FRULA')


if __name__ == '__main__':

    # list_solution()
    deque_solution()