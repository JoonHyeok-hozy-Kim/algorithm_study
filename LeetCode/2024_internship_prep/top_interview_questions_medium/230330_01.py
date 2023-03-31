from collections import deque

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:        
        M = {}
        text_list = []
        if numerator < 0 and denominator > 0:
            text_list.append('-')
            numerator *= -1
        elif numerator > 0 and denominator < 0:
            text_list.append('-')
            denominator *= -1
        elif numerator < 0 and denominator < 0:
            numerator *= -1
            denominator *= -1

        quotient = numerator // denominator
        remainder = numerator % denominator
        text_list.append(str(quotient))

        if remainder == 0:
            return ''.join(text_list)
        
        text_list.append('.')
        remainder *= 10
        while remainder != 0:
            # print('remainder : {}, text_list : {}, M : {}'.format(remainder, text_list, M))
            if remainder in M:
                infinite = deque()
                infinite.append(')')
                while len(text_list) != M[remainder] and text_list[-1] != '.':  
                    infinite.appendleft(text_list.pop())
                text_list.append('(')
                text_list.extend(infinite)
                break
            
            if remainder < denominator:
                M[remainder] = len(text_list)
                text_list.append('0')
                remainder *= 10
            else:
                quotient = remainder // denominator
                M[remainder] = len(text_list)
                text_list.append(str(quotient))
                remainder %= denominator
                if remainder == 0:
                    break
                else:
                    remainder *= 10
            
        return ''.join(text_list)

if __name__ == '__main__':
    s = Solution()
    # print(s.fractionToDecimal(1, 4))
    # print(s.fractionToDecimal(10, 400))

    
    # print(s.fractionToDecimal(1, 3))
    print(s.fractionToDecimal(4, 333))
    # print(s.fractionToDecimal(1, 7))
    # print(s.fractionToDecimal(123, 9900))
    
    # print(s.fractionToDecimal(22, 7))

    # print(s.fractionToDecimal(-1, -2147483648))
    print(s.fractionToDecimal(1, 17))


'''
2147483648
'''