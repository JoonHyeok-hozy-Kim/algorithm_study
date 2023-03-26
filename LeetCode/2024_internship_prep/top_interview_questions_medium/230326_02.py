class RandomizedSet:

    def __init__(self):
        self._map = {}
        self._data = []

    def insert(self, val: int) -> bool:
        if val in self._map:
            return False
        
        self._map[val] = len(self._data)
        self._data.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self._map:
            i = self._map[val]
            swap_val = self._data[-1]
            
            self._map[swap_val] = i
            del self._map[val]
            
            self._data[i] = swap_val
            self._data.pop()
            return True
            
            
        return False        

    def getRandom(self) -> int:
        return self._data[randint(0, len(self._data)-1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()