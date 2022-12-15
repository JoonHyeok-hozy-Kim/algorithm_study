"""
1932. 정수 삼각형
https://www.acmicpc.net/problem/1932
"""



if __name__ == '__main__':
    H = int(input())
    triangle = []
    for i in range(H):
        triangle.append(list(map(int, input().split())))

    for h in range(1, H):
        target_row = H-h-1
        for j in range(len(triangle[target_row])):
            triangle[target_row][j] += max(triangle[target_row+1][j], triangle[target_row+1][j+1])

    print(triangle[0][0])
