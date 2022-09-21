"""
1476. 날짜 계산
https://www.acmicpc.net/problem/1476
"""

def year_determinator(e, s, m):
    year = e
    s_false = True
    m_false = True

    year -= 15
    while s_false or m_false:
        year += 15
        s_false = False if (year-1)%28+1 == s else True
        if s_false:
            continue
        m_false = False if (year-1)%19+1 == m else True

    return year

if __name__ == '__main__':
    e, s, m = map(int, input().split())
    # print(e,s,m)
    print(year_determinator(e, s, m))