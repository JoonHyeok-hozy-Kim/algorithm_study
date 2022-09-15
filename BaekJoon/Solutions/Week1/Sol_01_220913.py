'''
1065. 한수
어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
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