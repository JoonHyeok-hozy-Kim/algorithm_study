from collections import deque

class User:
    def __init__(self, id):
        self._id = id
        self._followers = set()
    
    def follow(self, other):
        if other not in self._followers:
            self._followers.add(other)
    
    def shortest_path(self, other):
        Q = deque()
        for f in self._followers:
            Q.append((f, 1))
        while Q:
            popped, distance = Q.popleft()
            if popped == other:
                return distance
            for pf in popped._followers:
                Q.append((pf, distance+1))
        return -1
    
    def __str__(self):
        text_list = ['ID : ']
        text_list.append(str(self._id))
        text_list.append('\n')
        text_list.append('Followers : ')
        for f in self._followers:
            text_list.append(str(f._id))
            text_list.append(" ")
        text_list.append('\n')
        return ''.join(text_list)
    

if __name__ == '__main__':
    users = [User(i) for i in range(10)]    
    users[0].follow(users[1])
    users[1].follow(users[2])
    users[2].follow(users[3])
    users[3].follow(users[4])
    users[4].follow(users[5])
    
    users[0].follow(users[9])
    users[9].follow(users[5])
    # for u in users:
    #     print(u)

    print(users[0].shortest_path(users[5]))