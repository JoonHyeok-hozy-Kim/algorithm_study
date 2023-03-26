class Listy:
    class Node:
        def __init__(self, x):
            self._val = x
            self._prev = None
            self._next = None
        
        def add_next(self, N):
            self._next = N
            N._prev = self
    
    def __init__(self):
        self._header = None
        self._last = None
        self._size = 0
        self._map = {}
    
    def is_empty(self):
        return self._size == 0
    
    def append(self, v):
        new_node = self.Node(v)
        if self.is_empty():
            self._header = new_node
        else:
            self._last.add_next(new_node)
        self._last = new_node
        self._map[self._size] = new_node
        self._size += 1
    
    def element_at(self, i):
        if i >= self._size or i < 0:
            return -1
        return self._map[i]._val
    
    def pop(self):
        if self.is_empty():
            raise Exception('Empty')
        if self._header == self._last:
            self._header = None
            self._last = None
        else:
            self._last._next = None
        self._size -= 1
        del self._map[self._size]

    def __str__(self):
        text_list = ['[']
        walk = self._header
        while walk is not None:
            text_list.append(str(walk._val))
            text_list.append(', ')
            walk = walk._next
        text_list.pop()
        text_list.append(']')
        return ''.join(text_list)
    
    def search(self, v):
        idx = 0
        power = 1
        jdx = idx + power
        while True:
            e = self.element_at(jdx)
            if e == v:
                return jdx
            elif e == -1 or e > v:
                return self._binary_search(v, idx, jdx)
            else:
                idx = jdx
                power *= 2
                jdx += power
    
    def _binary_search(self, v, left, right):
        while left <= right:
            mid = (left + right) // 2
            e = self.element_at(mid)
            if e == v:
                return mid
            elif e > v:
                right = mid-1
            else:
                left = mid+1
        return -1


if __name__ == '__main__':
    l = Listy()
    for i in range(10):
        l.append(i)
        print(l)
    print(l.element_at(3))
    print(l.search(5))
    print(l.search(20))