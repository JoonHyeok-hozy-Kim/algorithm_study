"""
https://www.acmicpc.net/problem/24391
"""


if __name__ == '__main__':
    N, M = map(int, input().split())
    dp = [None] * (N+1)
    connected_id = 0
    connected_list = []
    for _ in range(M):
        i, j = map(int, input().split())

        if dp[i] is not None and dp[j] is not None and dp[i] != dp[j]:
            prev_j = dp[j]
            prev_j_set = connected_list[prev_j]
            for j_linked in prev_j_set:
                dp[j_linked] = dp[i]

            connected_list[dp[i]] = connected_list[dp[i]].union(prev_j_set)
            connected_list[prev_j] = None

        elif dp[i] is not None:
            dp[j] = dp[i]
            connected_list[dp[i]].add(j)

        elif dp[j] is not None:
            dp[i] = dp[j]
            connected_list[dp[j]].add(i)

        else:
            dp[i] = connected_id
            dp[j] = connected_id
            new_set = {i, j}
            connected_list.append(new_set)
            connected_id += 1

        # print(dp, connected_list)

    schedule = list(map(int, input().split()))
    # print(schedule)

    result = 0
    curr_building = dp[schedule[0]]
    for k in range(1, len(schedule)):
        # print('{} vs {}'.format(curr_building, dp[schedule[k]]))
        if curr_building is None or dp[schedule[k]] is None or dp[schedule[k]] != curr_building:
            result += 1
            curr_building = dp[schedule[k]]

    print(result)



"""
5 3
1 2
2 5
3 4
1 2 3 5 4

5 3
1 2
2 3
3 4
1 4 3 2 5

5 3
1 2
3 4
4 1
1 2 3 4 5

6 4
1 2
3 4
4 1
5 6
1 2 3 4 5 6

7 4
1 2
3 4
4 1
7 6
1 2 3 4 5 6 7

6 5
1 2
2 3
3 4
5 6
6 1
1 2 3 4 5 6
"""