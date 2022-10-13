"""
4889. 안정적인 문자열
https://www.acmicpc.net/problem/4889
"""



if __name__ == '__main__':
    T = 0
    while True:
        X = input()
        if X[0] == '-':
            break

        T += 1
        S = []
        for i in range(len(X)):
            if len(S) > 0 and X[i] == '}' and S[-1] == '{':
                S.pop()
            else:
                S.append(X[i])

        result = 0
        for i in range(len(S)//2):
            if S[i*2] == '}' and S[i*2+1] == '{':
                result += 2
            else:
                result += 1

        print('{}. {}'.format(T, result))

