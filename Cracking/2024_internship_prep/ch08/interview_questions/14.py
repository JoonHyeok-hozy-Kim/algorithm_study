def countEval(expr, value, M={}):
    if len(expr) == 1:
        if (expr == '1' and value) or (expr == '0' and not value):
            return 1
        else:
            return 0
    
    result = 0
    for i in range(1, len(expr), 2):
        operator = expr[i]
        left = expr[:i]
        right = expr[i+1:]
        
        tflr = [None] * 4
        cnt = 0
        for tf in (True, False):
            for lr in (left, right):
                if (tf, lr) not in M:
                    M[(tf, lr)] = countEval(lr, tf, M)
                tflr[cnt] = M[(tf, lr)]
                
        left_true, right_true, left_false, right_false = tflr

        if operator == '&':
            if value:
                result += left_true * right_true
            else:
                result += left_false * right_true
                result += left_true * right_false
                result += left_false * right_false
        elif operator == '|':
            if value:
                result += left_true * right_true
                result += left_false * right_true
                result += left_true * right_false
            else:
                result += left_false * right_false
        elif operator == '^':
            if value:
                result += left_false * right_true
                result += left_true * right_false
            else:
                result += left_true * right_true
                result += left_false * right_false
        else:
            raise Exception("Undefined operator.")
    
    # print('{} / {} / {}'.format(expr, value, result))
    return result


if __name__ == '__main__':
    print(countEval("1|0&0", False))
    print(countEval("1^0|0|1", False))
    print(countEval("0&0&0&1^1|0", True))