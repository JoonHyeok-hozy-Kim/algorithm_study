"""
4658. 삼각형 게임
https://www.acmicpc.net/problem/4658
"""

def flip_play(T, prev_t=None, cnt=0, inner_list=None, answer=0):
    for i in range(cnt): print(' ', end="")
    print('In flip_play, cnt : {}, prev_t : {}, inner_list : {}'.format(cnt, prev_t, inner_list))

    if cnt == 7:
        temp_sum = 0
        for t in T:
            temp_sum += sum(t[1])
        temp_sum -= sum(inner_list)*2
        print('--> In final, temp_sum : {}'.format(temp_sum))
        return True, temp_sum

    elif cnt == 6:
        first_i = None
        final_go_on = False
        for i in range(6):
            if T[i][0] == -1:
                first_i = i

        if first_i is None:
            return False, 0

        for first_s in T[first_i][1]:
            if first_s != inner_list[0]:
                for last_s in prev_t:
                    if last_s != inner_list[-1] and last_s == first_s:
                        inner_list[cnt-1] = last_s
                        go_on, temp_answer = flip_play(T, prev_t, cnt + 1, inner_list, answer)
                        if go_on:
                            answer = max(answer, temp_answer)
                            final_go_on = go_on
                        inner_list[cnt-1] = None
        return final_go_on, answer

    elif cnt == 0:
        inner_list = [None] * 6
        curr_t = T[0][1]
        T[0][0] = -1
        go_on, temp_answer = flip_play(T, curr_t, cnt + 1, inner_list, answer)
        if go_on:
            return True, max(answer, temp_answer)
        else:
            return False, 0

    else:
        for prev_s in prev_t:
            for i in range(6):
                if T[i][0] == 0:
                    for curr_s in T[i][1]:
                        if prev_s == curr_s != inner_list[cnt-2]:
                            curr_t = T[i][1]
                            T[i][0] = 1
                            inner_list[cnt-1] = prev_s
                            go_on, temp_answer = flip_play(T, curr_t, cnt + 1, inner_list, answer)
                            if go_on:
                                answer = max(temp_answer, answer)

                            T[i][0] = 0
                            inner_list[cnt-1] = None

        return True, answer



def turn_play(T, curr_s=None, cnt=0, inner_list=None, answer=None):
    # for i in range(cnt): print(' ', end="")
    # print('In turn_play, cnt : {}, curr_s : {}, inner_list : {}'.format(cnt, curr_s, inner_list))

    if cnt == 0:
        inner_list = [None] * 6
        curr_t = T[0][1]
        T[0][0] = -1
        for i in range(3):
            curr_s = curr_t[i]
            last_s = curr_t[(i+1)%3]
            inner_list[cnt] = curr_s
            inner_list[-1] = last_s
            # print('curr_t : {}, next_s : {}'.format(curr_t, curr_s))
            go_on, temp_answer = turn_play(T, curr_s, cnt+1, inner_list, answer)
            if go_on:
                answer = max(answer, temp_answer) if answer is not None else temp_answer
            inner_list[cnt] = None
            inner_list[-1] = None


    for i in range(1, 6):
        if T[i][0] == 0:
            for j in range(3):
                if T[i][1][j] == curr_s:
                    next_s = T[i][1][(j+2)%3]
                    # for m in range(cnt): print(' ', end="")
                    # print('curr_t : {}, next_s : {}'.format(T[i][1], next_s))

                    if cnt == 5:
                        if next_s == inner_list[-1]:
                            s_sum = 0
                            for l in range(6):
                                s_sum += sum(T[l][1])
                            s_sum -= sum(inner_list)*2
                            # print('FINAL : {}'.format(s_sum))
                            answer = max(answer, s_sum) if answer is not None else s_sum
                            return True, answer

                        return False, answer


                    T[i][0] = 1
                    inner_list[cnt] = next_s
                    go_on, temp_answer = turn_play(T, next_s, cnt + 1, inner_list, answer)
                    if go_on:
                        answer = max(temp_answer, answer) if answer is not None else temp_answer
                    T[i][0] = 0
                    inner_list[cnt] = None

    return True, answer



if __name__ == '__main__':
    T = []
    answers = []
    while True:
        text = input()
        if text == '*':
            # print('Start flip_play at *')
            finale, answer = turn_play(T)
            answers.append(answer)
            T.clear()
        elif text == '$':
            # print('Start flip_play at $')
            finale, answer = turn_play(T)
            answers.append(answer)
            break
        else:
            T.append([0, list(map(int, text.split()))])

    # print(*answers, sep="\n")
    for a in answers:
        print(a) if a is not None else print('none')