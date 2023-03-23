def bubble_sort(S: list) -> None:
    for i in range(1, len(S)):
        curr = S[i]
        j = i
        while j > 0 and S[j-1] > curr:
            S[j] = S[j-1]
            j -= 1
        S[j] = curr
        print('i : {}, curr : {}, S : {}'.format(i, curr, S))


if __name__ == '__main__':
    a = [3,3,8,9,7,1,5,7,8,1,2,3,4,5,3,2]
    bubble_sort(a)