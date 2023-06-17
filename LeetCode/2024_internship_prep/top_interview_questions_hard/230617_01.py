class LRUCache:
    
    '''
    Map : self._keys = {key : [value, Node]}
    
    Node : Linked list
    
    (head) - (Node1) - (Node2) - ... - (NodeCapacity) - (tail)
     <- recent <-                                              
    
    '''
    
    class Node:
        def __init__(self, key, prev=None, next=None):
            self._key = key
            self._prev = prev
            if prev:
                prev._next = self
            self._next = next
            if next:
                next._prev = self
        
        def move_after(self, to_prev):
            self._prev._next = self._next
            self._next._prev = self._prev
            
            to_prev_next = to_prev._next
            to_prev._next = self
            self._prev = to_prev
            self._next = to_prev_next
            to_prev_next._prev = self
            

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._keys = {}
        self._log_head = self.Node(None)
        self._log_tail = self.Node(None, self._log_head)
        

    def get(self, key: int) -> int:
        if key not in self._keys:
            return -1
        
        self._keys[key][1].move_after(self._log_head)
        return self._keys[key][0]
        

    def put(self, key: int, value: int) -> None:
        if key in self._keys:
            self._keys[key][0] = value
            self._keys[key][1].move_after(self._log_head)
        
        elif len(self._keys) < self._capacity:
            self._keys[key] = [value, self.Node(key, self._log_head, self._log_head._next)]
        
        else:
            last_log = self._log_tail._prev
            del self._keys[last_log._key]
            last_log._key = key
            self._keys[key] = [value, last_log]
            last_log.move_after(self._log_head)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)