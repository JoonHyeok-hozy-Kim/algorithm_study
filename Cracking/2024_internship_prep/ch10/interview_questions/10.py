from bisect import bisect_left, bisect_right

class Stream:
    def __init__(self):
        self._stream = []
    
    def add(self, val):
        if len(self._stream) == 0:
            self._stream.append(val)
        else:
            if val < self._stream[0]:
                self._stream.insert(0, val)
            elif val > self._stream[-1]:
                self._stream.append(val)
            else:
                i = bisect_right(self._stream, val)
                self._stream.insert(i, val)
    
    def get_rank_of_number(self, num):
        return bisect_right(self._stream, num)-1


class TreeStream:
    class Node:
        def __init__(self, v):
            self._val = v
            self._left = None
            self._right = None
            self._children_cnt = 0
    
    def __init__(self):
        self._root = None
    
    def add(self, v):
        if self._root is None:
            self._root = self.Node(v)
            return self._root
        
        walk = self._root
        while walk is not None:
            walk._children_cnt += 1
            if v <= walk._val:
                if walk._left is None:
                    walk._left = self.Node(v)
                    return walk._left
                else:
                    walk = walk._left
            else:
                if walk._right is None:
                    walk._right = self.Node(v)
                    return walk._right
                else:
                    walk = walk._right
    
    def get_rank_of_number(self, num):
        result = 0
        walk = self._root
        while walk._val != num:
            if walk._val > num:
                walk = walk._left
            else:
                result += 1
                if walk._left:
                    result += walk._left._children_cnt + 1
                walk = walk._right
        
        if walk._left:
            result += walk._left._children_cnt + 1
        
        return result

    def inorder_traversal(self, node=None, depth=0):
        if node is None:
            node = self._root
        
        if node._left:
            self.inorder_traversal(node._left, depth+1)
        print('{}({}, {})'.format(node._val, depth, node._children_cnt), end =" ")
        if node._right:
            self.inorder_traversal(node._right, depth+1)

if __name__ == '__main__':
    a = [5,1,4,4,5,9,7,13,3]
    # s = Stream()
    # for n in a:
    #     s.add(n)
    #     print(s._stream)
    # print(s.get_rank_of_number(1))
    # print(s.get_rank_of_number(3))
    # print(s.get_rank_of_number(4))

    s = TreeStream()
    for n in a:
        s.add(n)
    # s.inorder_traversal()
    print(s.get_rank_of_number(1))
    print(s.get_rank_of_number(3))
    print(s.get_rank_of_number(4))