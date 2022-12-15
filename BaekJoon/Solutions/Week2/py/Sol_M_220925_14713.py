"""
14713. 앵무새
https://www.acmicpc.net/problem/14713
"""

if __name__ == '__main__':
    N = int(input())
    word_map = {}
    word_cnt = 0
    for i in range(N):
        sentence = input().split()
        count = 0
        for word in sentence:
            if word not in word_map:
                word_map[word] = []
            word_map[word].append((i, count))
            count += 1
        word_cnt += count

    target = list(input().split())
    status = [0 for _ in range(N)]

    possible_flag = True
    correct_cnt = 0
    for word in target:
        if word not in word_map:
            possible_flag = False
            break

        temp_list = word_map[word]
        success = False
        for s in temp_list:
            if status[s[0]] == s[1]:
                status[s[0]] += 1
                success = True
                correct_cnt += 1
                break
        if not success:
            possible_flag = False
            break

    if word_cnt != correct_cnt:
        possible_flag = False

    print('Possible') if possible_flag else print('Impossible')