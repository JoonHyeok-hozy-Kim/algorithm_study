

def binary_to_string(A: float) -> str:
    result_list = ["0."]
    power = 0.5
    for i in range(32):
        if A >= power:
            result_list.append("1")
            A -= power
        if A == 0:
            break
        power /= 2
    
    if A > 0:
        return "ERROR"
    else:
        return ''.join(result_list)

if __name__ == '__main__':
    print(binary_to_string(.72))
    print(binary_to_string(.75))
    