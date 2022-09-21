'''
1065. 한수
https://www.acmicpc.net/problem/1065
'''

def hansoo(N):
    '''
    :param N: integer less than or equal to 1000
    :return: Let hansoo, a number that each digit forms an arithmetic progression. Return the number of hansoos that
             are less than or equal to N.
    '''
    result = 0
    for i in range(1, 10):
        if i <= N:
            result += 1
            for j in range(0, 10):
                result += _hansoo_generator(i, j, N, 0)
                if j > 0:
                    result += _hansoo_generator(i, j*(-1), N, 0)
    return result

def _hansoo_generator(current_num, d, upper_bound, count):
    last_digit = current_num%10
    current_num *= 10
    last_digit += d
    if last_digit < 0 or last_digit > 9:
        return count
    current_num += last_digit
    if current_num > upper_bound:
        return count

    # print('{} counted'.format(current_num))
    return _hansoo_generator(current_num, d, upper_bound, count+1)


if __name__ == '__main__':
    print(hansoo(int(input())))