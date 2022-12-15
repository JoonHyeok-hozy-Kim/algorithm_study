"""
11277. 2-SAT - 1
https://www.acmicpc.net/problem/11277
"""

def determine_clause(N, clause):
    a = N & (1<<(abs(clause[0])-1))
    b = N & (1<<(abs(clause[1])-1))

    if clause[0] < 0:
        a = not a
    if clause[1] < 0:
        b = not b
    # print(a, b)
    return a | b


def loop_solution(N, C):
    for n in range((1<<N+1)-1):
        success = False
        for clause in C:
            if determine_clause(n, clause):
                success = True
            else:
                success = False
                break
        if success:
            return True
    return False


if __name__ == '__main__':
    N, M = map(int, input().split())
    clauses = [list(map(int, input().split())) for _ in range(M)]
    # print(clauses)

    print(1) if loop_solution(N, clauses) else print(0)