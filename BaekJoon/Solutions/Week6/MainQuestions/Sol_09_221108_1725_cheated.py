"""
https://www.acmicpc.net/problem/1725
"""

def DNC_solution(B):
    if len(B) == 1:
        # print(B, B[0])
        return B[0]

    mid = len(B) // 2
    candidates = []
    B1 = B[:mid]
    B2 = B[mid:]

    candidates.append(DNC_solution(B1))
    candidates.append(DNC_solution(B2))

    left, right = mid-1, mid
    mid_height = min(B[left], B[right])
    temp_area = 2 * mid_height
    while left > 0 or right < len(B)-1:
        if left == 0:
            right += 1
        elif right == len(B) - 1:
            left -= 1
        else:
            if B[left-1] > B[right+1]:
                left -= 1
            else:
                right += 1
        mid_height = min(mid_height, B[left], B[right])
        # print('B : {}, temp_area : {} / left : {}, right : {}, mid_height : {}, val : {}'.format(
        #     B, temp_area, left, right, mid_height, mid_height * (right-left+1)
        # ))
        temp_area = max(temp_area, mid_height * (right-left+1))

    candidates.append(temp_area)

    # print(B, max(candidates), candidates)

    return max(candidates)


if __name__ == '__main__':
    N = int(input())
    bars = [int(input()) for _ in range(N)]
    # print(bars)

    result = DNC_solution(bars)
    print(result)