"""
https://www.acmicpc.net/problem/2011
"""


def recursive_parse(N, cnt=0):
    if cnt == len(N):
        # print('ADDED')
        return 1
    elif cnt > len(N):
        return 0

    result = 0
    if int(N[cnt]) == 1:
        if cnt < int(len(N))-1 and int(N[cnt + 1]) == 0:
            result += recursive_parse(N, cnt + 2)

        else:
            result += recursive_parse(N, cnt+1)
            result += recursive_parse(N, cnt+2)

    elif int(N[cnt]) == 2:
        if cnt < int(len(N))-1 and int(N[cnt+1]) == 0:
            result += recursive_parse(N, cnt+2)

        elif cnt < int(len(N))-1 and int(N[cnt+1]) <= 6:
            result += recursive_parse(N, cnt+1)
            result += recursive_parse(N, cnt+2)

        else:
            result += recursive_parse(N, cnt+1)

    else:
        result += recursive_parse(N, cnt+1)

    return result


def get_fibonacci_list(n):
    result = []
    for i in range(2):
        result.append(i+1)
        if n == i+1:
            return result
    for i in range(n-2):
        val = result[-2] + result[-1]
        result.append(val)

    return result


def get_partition(N):
    result = []
    cnt = 0
    max_cnt = 0
    i = len(N)
    while i > 0:
        i -= 1
        # print('N[{}] : {}, cnt : {}'.format(i, N[i], cnt))
        if int(N[i]) == 0:
            if i > 0 and int(N[i-1]) in (1, 2):
                if cnt > 0:
                    result.append(cnt)
                    max_cnt = max(max_cnt, cnt)
                    cnt = 0

            else:
                return [], 0

        elif int(N[i]) in (1, 2):
            if i < len(N)-1 and int(N[i+1]) == 0:
                result.append(1)
                max_cnt = max(max_cnt, 1)
                cnt = 0

            else:
                cnt += 1

        elif i > 0 and int(N[i-1]) == 1:
            if cnt > 0:
                result.append(cnt)
                max_cnt = max(max_cnt, cnt)
                cnt = 0
            cnt += 1

        elif i > 0 and int(N[i-1]) == 2:
            if int(N[i]) <= 6:
                # print('PT4-1')
                if cnt > 0:
                    result.append(cnt)
                    max_cnt = max(max_cnt, cnt)
                    cnt = 0
                cnt += 1

            else:
                # print('PT4-1')
                if cnt > 0:
                    result.append(cnt)
                    max_cnt = max(max_cnt, cnt)
                result.append(1)
                max_cnt = max(max_cnt, 1)
                cnt = 0

        else:
            # print('PT5')
            if cnt > 0:
                result.append(cnt)
                max_cnt = max(max_cnt, cnt)
            result.append(1)
            cnt = 1

        if i == 0 and cnt > 0:
            result.append(cnt)
            max_cnt = max(max_cnt, cnt)
        # print(result)

    return result, max_cnt


if __name__ == '__main__':
    num_text = input()

    # result = recursive_parse(num_text)

    # print(get_fibonacci_list(10))
    P, fibo_max = get_partition(num_text)
    # print(P)
    F = get_fibonacci_list(fibo_max)

    if len(P) == 0:
        print(0)

    else:
        result = 1
        for p in P:
            result *= F[p-1]
            if result > 1000000:
                result %= 1000000
        print(result % 1000000)