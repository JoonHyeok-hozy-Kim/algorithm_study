# 4,000,000,000 * 4B = 16,000,000,000B = 16GB


class ExclusiveNumSet:
    def __init__(self, min):
        self._min = min
        self._max = -1
        self._set = set()
    
    def add_num(self, val):
        if self._max == -1:
            for i in range(self.min+1, val):
                self._set.add(i)
        elif val > self._max:
            for i in range(self._max+1, val):
                self._set.add(i)
            self._max = val
        elif val in self._set:
            self._set.remove(val)

class MissingInt:
    def __init__(self):
        self._num_sets = []
    

if __name__ == '__main__':
    e = ExclusiveNumSet()
    e.add_num(5)
    print(e._set)
    e.add_num(6)
    print(e._set)
    e.add_num(10)
    print(e._set)
    e.add_num(3)
    print(e._set)