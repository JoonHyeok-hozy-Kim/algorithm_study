from collections import deque

def sqrt(x):
    left, right = 0, x
    while left <= right:
        mid = (left+right) // 2
        sq = mid * mid
        if sq == x:
            return mid
        elif sq > x:
            right = mid-1
        else:
            left = mid + 1
    return left-1

if __name__ == '__main__':
    for i in range(100, 1000):
        s = sqrt(i)
        print(i, s, s**2)