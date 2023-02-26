def get_unique_bottle(bottles: list) -> int:
    weight = 0.0
    power = 1
    for i in range(len(bottles)):
        weight += bottles[i] * power
        power *= 10

    # print(weight)
    if weight - int(weight) > 0:
        return 1
    else:
        cnt = 2
        int_weight = int(weight)
        while int_weight > 0:
            if int_weight % 10 == 2:
                return cnt
            else:
                int_weight //= 10
                cnt += 1

    return None

if __name__ == '__main__':
    bottle_cnt = 5
    B = [1.0] * bottle_cnt
    print(B)
    for i in range(bottle_cnt):
        B[i] = 1.1
        print(B)
        print(f"answer : {i+1}, result : {get_unique_bottle(B)}")
        B[i] = 1.0