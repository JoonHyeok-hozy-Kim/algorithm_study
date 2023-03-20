def duplicated(u1, u2):
    w1 = u1.split('/')
    w2 = u2.split('/')
    if len(w1) != len(w1):
        return False
    
    for i, v in enumerate(w1):
        if v != w2[i]:
            return False
    
    return True


class URL_Tree:
    def __init__(self):
        self._tree = {}
    
    def exists(self, u):
        M = self._tree
        for w in u.split('/'):
            if w not in M:
                return False
            M = M[w]
        return True
    
    def add_url(self, u):
        M =self._tree
        for w in u.split('/'):
            if w not in M:
                M[w] = {}
            M = M[w]


if __name__ == "__main__":
    T = URL_Tree()

    u1 = "www.naver.com/main"
    u2 = "www.naver.com/login"
    
    print(T.exists(u1))
    T.add_url(u1)
    print(T.exists(u1))
    print(T.exists(u2))
    T.add_url(u2)

    u3 = "www.naver.com"
    print(T.exists(u3))

    u4 = "www.google.com"
    print(T.exists(u4))