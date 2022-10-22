"""
https://www.acmicpc.net/problem/2628
"""

if __name__ == '__main__':
    width, height = map(int, input().split())
    cut_cnt = int(input())
    cuts = {'h': [], 'v': []}
    for _ in range(cut_cnt):
        a, b = map(int, input().split())
        if a == 0:
            cuts['h'].append(b)
        else:
            cuts['v'].append(b)

    cuts['h'].sort()
    cuts['v'].sort()
    # print(cuts)

    if len(cuts['h']) == 0:
        max_height = height
    else:
        max_height = max(cuts['h'][0], height - cuts['h'][-1])
        if len(cuts['h']) > 1:
            for i in range(len(cuts['h'])-1):
                max_height = max(cuts['h'][i+1] - cuts['h'][i], max_height)

    if len(cuts['v']) == 0:
        max_width = width
    else:
        max_width = max(cuts['v'][0], width - cuts['v'][-1])
        if len(cuts['v']) > 1:
            for i in range(len(cuts['v'])-1):
                max_width = max(cuts['v'][i+1] - cuts['v'][i], max_width)

    # print(max_width, max_height)
    print(max_width * max_height)