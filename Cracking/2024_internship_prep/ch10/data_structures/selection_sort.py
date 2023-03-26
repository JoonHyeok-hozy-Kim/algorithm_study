def selection_sort(S: list) -> None:
    for i in range(len(S)):
        min_idx, min_val = i, S[i]
        j = i
        while j < len(S):
            if S[j] < min_val:
                min_idx, min_val = j, S[j]
            j += 1
        S[i], S[min_idx] = S[min_idx], S[i]
        print('i : {}, min_val : {}, S : {}'.format(i, min_val, S))


if __name__ == '__main__':
    a = [3,3,8,9,7,1,5,7,8,1,2,3,4,5,3,2]
    selection_sort(a)