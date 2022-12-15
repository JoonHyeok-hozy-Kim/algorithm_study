"""
12852. 1로 만들기 2
https://www.acmicpc.net/problem/12852
"""

def get_sequence(n):
    cnt_list = [0, 0, 1]
    opr_list = [0, 1, 2]
    if n > 2:
        num = 2
        while num != n:
            num += 1
            if num % 6 == 0:
                a = cnt_list[num-1]
                b = cnt_list[num//2]
                c = cnt_list[num//3]
                m = min(a, b, c)
                if m == c:
                    cnt_list.append(cnt_list[num//3] + 1)
                    opr_list.append(3)
                elif m == b:
                    cnt_list.append(cnt_list[num//2] + 1)
                    opr_list.append(2)
                else:
                    cnt_list.append(cnt_list[num-1] + 1)
                    opr_list.append(1)
            elif num % 3 == 0:
                a = cnt_list[num-1]
                b = cnt_list[num//3]
                if a >= b:
                    cnt_list.append(cnt_list[num//3] + 1)
                    opr_list.append(3)
                else:
                    cnt_list.append(cnt_list[num-1] + 1)
                    opr_list.append(1)
            elif num % 2 == 0:
                a = cnt_list[num-1]
                b = cnt_list[num//2]
                if a >= b:
                    cnt_list.append(cnt_list[num//2] + 1)
                    opr_list.append(2)
                else:
                    cnt_list.append(cnt_list[num-1] + 1)
                    opr_list.append(1)
            else:
                cnt_list.append(cnt_list[num-1] + 1)
                opr_list.append(1)

    print(cnt_list[n])
    k = n
    while k > 0:
        print(k, end=" ")
        if opr_list[k] == 3:
            k //= 3
        elif opr_list[k] == 2:
            k //= 2
        else:
            k -= 1

if __name__ == '__main__':
    N = int(input())

    get_sequence(N)