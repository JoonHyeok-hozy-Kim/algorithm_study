"""
https://www.acmicpc.net/problem/14713
"""

from collections import deque


def solution():
    N = int(input())
    parrots = [deque(input().split()) for _ in range(N)]
    question = deque(input().split())
    # print(parrots)
    # print(question)

    while len(question) > 0:
        target = question[0]
        fail = True
        candidates = []
        for i in range(N):
            if len(parrots[i]) > 0 and parrots[i][0] == target:
                candidates.append(i)

        # print(candidates)
        if len(candidates) == 0:
            break

        elif len(candidates) == 1:
            parrots[candidates[0]].popleft()
            fail = False

        else:
            remainings = [[] for _ in range(len(candidates))]
            max_len = 0
            for j in range(len(candidates)):
                max_len = max(max_len, len(parrots[candidates[j]]))
                for w in parrots[candidates[j]]:
                    if w in question:
                        idx = question.index(w)
                    # print(w, idx)
                    if idx >= 0:
                        remainings[j].append(idx)

            cnt = 1
            min_info = [None, None]
            for _ in range(max_len):
                if min_info[0] is not None:
                    break
                for k in range(len(candidates)):
                    if len(remainings[k]) > cnt:
                        if min_info[0] is None or min_info[1] > remainings[k][cnt]:
                            min_info = [candidates[k], remainings[k][cnt]]
                        elif min_info[1] == remainings[k][cnt]:
                            min_info = [None, None]
                            cnt += 1
                            break

            if min_info[0] is not None:
                parrots[min_info[0]].popleft()
                fail = False
            else:
                parrots[candidates[0]].popleft()
                fail = False


        if not fail:
            question.popleft()

    if fail:
        print('Impossible')
        return
    else:
        for p in parrots:
            if len(p) > 0:
                print('Impossible')
                return
        print('Possible')

if __name__ == '__main__':
    solution()