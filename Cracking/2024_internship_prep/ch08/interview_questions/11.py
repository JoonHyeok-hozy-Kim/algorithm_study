from copy import deepcopy

COINS = (1, 5, 10, 25)
CHANGES_RECORD = {}

def ways_to_pay(amount):
    result = 0
    for i in range(amount//COINS[3]+1):
        result += make_changes(amount, 3, i)
    return result


def make_changes(amount, cidx, cnt, depth=0):
    if cidx < 0:
        return 0
    
    for i in range(depth):
        print("  ", end="")
    print('In make_changes, amount : {}, coin : {}, cnt : {}'.format(amount, COINS[cidx], cnt))
    new_amount = amount - COINS[cidx] * cnt
    if new_amount < 0:
        result = 0
    elif new_amount == 0:
        result = 1
    else:
        result = 0
        for i in range(new_amount//COINS[cidx-1] + 1):
            if (new_amount, cidx-1, i) in CHANGES_RECORD:
                result += CHANGES_RECORD[(new_amount, cidx-1, i)]
            else:
                result += make_changes(new_amount, cidx-1, i, depth+1)

    CHANGES_RECORD[(amount, cidx, cnt)] = result
    return result
    



if __name__ == '__main__':
    print(ways_to_pay(50))