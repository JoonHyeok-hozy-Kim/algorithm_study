"""
1062. 가르침
https://www.acmicpc.net/problem/1062
"""
from copy import deepcopy
PRE_SUFFIX = "antic"


def recursive_char_comb(word_map, char_keys, target_cnt, char_comb=[], i=0, cnt=0, max_val=0):
    if cnt == target_cnt:
        cand = get_possible_words(word_map, char_comb)
        # print('cand : {}, char_comb : {}'.format(cand, char_comb))
        return max(max_val, cand)
    if i == len(char_keys):
        return max_val

    c_char_comb = deepcopy(char_comb)
    cand1 = recursive_char_comb(word_map, char_keys, target_cnt, c_char_comb, i+1, cnt)

    char_comb.append(char_keys[i])
    cand2 = recursive_char_comb(word_map, char_keys, target_cnt, char_comb, i+1, cnt+1)

    return max(cand1, cand2)


def get_possible_words(word_map, char_comb):
    word_cnt = 0
    for word in word_map:
        total_char = len(word_map[word])
        cnt = 0
        for c in char_comb:
            if c in word:
                cnt += 1
        if total_char == cnt:
            word_cnt += 1
    return word_cnt


if __name__ == '__main__':
    N, K = map(int, input().split())
    char_map = {}
    word_map = {}
    for i in range(N):
        word = input()
        word = word[4:len(word)-4]
        word_map[word] = {}
        for c in word:
            if c not in PRE_SUFFIX:
                if c not in char_map:
                    char_map[c] = {}
                char_map[c][word] = True
                word_map[word][c] = True

    # print('char_map : {}'.format(char_map))
    # print('word_map : {}'.format(word_map))

    if K - len(PRE_SUFFIX) >= len(char_map):
        print(len(word_map))
    else:
        char_keys = list(char_map.keys())
        result = recursive_char_comb(word_map, char_keys, K - len(PRE_SUFFIX))
        print(result)
