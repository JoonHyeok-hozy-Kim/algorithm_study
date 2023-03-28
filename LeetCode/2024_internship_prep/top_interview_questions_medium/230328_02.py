class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result = 0
        sign = 1
        
        if dividend < 0:
            dividend = -dividend
            if divisor > 0:
                sign = -1
            else:
                divisor = -divisor
        else:
            if divisor < 0:
                divisor = -divisor
                sign = -1
        
        print('dividend : {}, divisor : {}'.format(dividend, divisor))
        d = divisor
        while d << 1 <= dividend:
            d <<= 1
            print('d : {}'.format(d))
        
        while dividend >= 0 and d >= divisor:
            result <<= 1
            if dividend >= d:
                result += 1
                dividend -= d
            d >>= 1
            print('result : {}'.format(result))
        
        return result * sign


if __name__ == '__main__':
    s = Solution()
    print(s.divide(-2147483648, -1))