"""
1041. 주사위
https://www.acmicpc.net/problem/1041
"""


THREE_SET = (
    '043',
    '042',
    '013',
    '012',
    '543',
    '542',
    '513',
    '512',
)



def get_min_num_cases(D):

    min_two = None
    for i in range(6):
        for j in range(6):
            if i != j and i+j != 5:
                temp = D[i]+D[j]
                min_two = min(min_two, temp) if min_two is not None else temp

    min_three = None
    for set in THREE_SET:
        temp = D[int(set[0])]+D[int(set[1])]+D[int(set[2])]
        min_three = min(min_three, temp) if min_three is not None else temp


    return [min(D), min_two, min_three]



if __name__ == '__main__':
    N = int(input())
    dice = list(map(int, input().split()))

    # print(dice)

    if N == 1:
        result = sum(dice) - max(dice)

    else:
        case_one, case_two, case_three = get_min_num_cases(dice)
        # print(case_one, case_two, case_three)

        result = 4 * case_three
        result += 4 * (N-1 + N-2) * case_two
        result += (4 * (N-1) + (N-2)) * (N-2) * case_one

    print(result)


"""
Combination Types

A B C D E F
0 1 2 3 4 5

AED 043
AEC 042
ABD 013
ABC 012
FED 543
FEC 542
FBD 513
FBC 512

"""