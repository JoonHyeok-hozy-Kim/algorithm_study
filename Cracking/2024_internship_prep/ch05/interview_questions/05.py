"""
1000 -> 111
1100 -> 1011
1111 -> 1110

Check whether the given input number is a power of 2
"""

def power_of_two(N: int) -> bool:
    return N & N-1 == 0

if __name__ == '__main__':
    for i in range(100):
        print("{} - {}".format(i, power_of_two(i)))