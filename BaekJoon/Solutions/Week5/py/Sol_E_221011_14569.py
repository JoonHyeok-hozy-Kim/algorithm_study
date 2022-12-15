"""
14569. 시간표 짜기
https://www.acmicpc.net/problem/14569
"""


if __name__ == '__main__':
    N = int(input())
    classes = [list(map(int, input().split())) for _ in range(N)]
    M = int(input())
    for _ in range(M):
        class_cnt = [0] * N
        excluded_class = []
        student_input = map(int, input().split())
        loop_cnt = 0
        for j in student_input:
            if loop_cnt == 0:
                for c in classes:
                    if j < c[0]:
                        excluded_class.append(c)
            else:
                for k in range(N):
                    if k not in excluded_class and j in classes[k][1:]:
                        class_cnt[k] += 1
            loop_cnt += 1

        result_cnt = 0
        for k in range(N):
            if class_cnt[k] == classes[k][0]:
                result_cnt += 1
        print(result_cnt)