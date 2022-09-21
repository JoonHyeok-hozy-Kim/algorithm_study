'''
1181. 단어정렬
https://www.acmicpc.net/problem/1181
'''

def compare_words_small(W, Y):
    w_list = list(W)
    y_list = list(Y)
    if len(w_list) < len(y_list):
        return W
    elif len(w_list) > len(y_list):
        return Y

    n = len(w_list)
    for i in range(n):
        if w_list[i] < y_list[i]:
            return W
        elif w_list[i] > y_list[i]:
            return Y
    return W


def _merge_array(S1, S2, S):
    i = j = 0
    while i+j < len(S):
        if j == len(S2) or (i<len(S1) and compare_words_small(S1[i], S2[j]) == S1[i]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1

def merge_sort_array(S):
    n = len(S)
    if n < 2:
        return

    mid = n//2
    S1 = S[0:mid]
    S2 = S[mid:n]

    merge_sort_array(S1)
    merge_sort_array(S2)
    _merge_array(S1, S2, S)

if __name__ == '__main__':
    word_cnt = int(input())
    word_list = []
    for i in range(word_cnt):
        word_list.append(input())
    merge_sort_array(word_list)
    if len(word_list) > 0:
        idx = 0
        while True:
            if idx == len(word_list)-1:
                break
            if word_list[idx] == word_list[idx+1]:
                word_list.pop(idx+1)
            else:
                idx += 1
    for word in word_list:
        print(word)