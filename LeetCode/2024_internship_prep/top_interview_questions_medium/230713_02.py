class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Search the least used character : word[mi]
        M = defaultdict(list)
        D = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        for i, c in enumerate(word):
            M[c].append(i)
        mc, mi = inf, None
        for c in M:
            if len(M[c]) < mc:
                mc, mi = len(M[c]), M[c][0]
        
        print('mi : {}'.format(mi))
        # [0, i1, j1, i2, j2, set([i, j])]
        Q = deque()
        for i, r in enumerate(board):
            for j, v in enumerate(r):
                if v == word[mi]:
                    Q.append([1, i, j, i, j, set([(i, j)])])
        
        while Q:
            # print(Q[0])
            dpth, i1, j1, i2, j2, s = Q.popleft()
            if mi-dpth < 0 and mi+dpth >= len(word):
                print(dpth, i1, j1, i2, j2, s)
                return True
            
            p1_set, p2_set = [], []
            for d in D:
                if mi-dpth >= 0:
                    di, dj = i1+d[0], j1+d[1]
                    if 0 <= di < len(board) and 0 <= dj < len(board[0]):
                        if (di, dj) not in s and board[di][dj] == word[mi-dpth]:
                            p1_set.append([di, dj])
                if mi+dpth < len(word):
                    di, dj = i2+d[0], j2+d[1]
                    if 0 <= di < len(board) and 0 <= dj < len(board[0]):
                        if (di, dj) not in s and board[di][dj] == word[mi+dpth]:
                            p2_set.append([di, dj])
            
            print('p1_set : {}, p2_set : {}'.format(p1_set, p2_set))
            if mi-dpth < 0 and len(p1_set) == 0:
                for [pi2, pj2] in p2_set:
                    temp_set = deepcopy(s)
                    temp_set.add((pi2, pj2))
                    Q.append([dpth+1, i1, j1, pi2, pj2, temp_set])
            elif mi+dpth >= len(word) and len(p2_set) == 0:
                for [pi1, pj1] in p1_set:
                    temp_set = deepcopy(s)
                    temp_set.add((pi1, pj1))
                    Q.append([dpth+1, pi1, pj1, i2, j2, temp_set])
            elif len(p1_set) > 0 and len(p2_set) > 0:
                for [pi2, pj2] in p2_set:
                    for [pi1, pj1] in p1_set:
                        if pi1 == pi2 and pj1 == pj2:
                            continue
                        temp_set = deepcopy(s)
                        temp_set.add((pi1, pj1))
                        temp_set.add((pi2, pj2))
                        Q.append([dpth+1, pi1, pj1, pi2, pj2, temp_set])
        
        return False
                        