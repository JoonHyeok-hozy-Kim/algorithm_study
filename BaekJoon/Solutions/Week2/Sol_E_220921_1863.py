"""
1863. 스카이라인 쉬운거

https://www.acmicpc.net/problem/1863
"""

if __name__ == '__main__':
    N = int(input())
    heights = []
    result = 0
    for i in range(N):
        h = list(map(int, input().split()))[1]
        if h == 0:
            if len(heights) > 0:
                result += len(heights)
                heights.clear()
        else:
            while len(heights) > 0 and heights[-1] > h:
                result += 1
                heights.pop()
            if len(heights) == 0 or heights[-1] < h:
                heights.append(h)

    result += len(heights)

    print(result)
