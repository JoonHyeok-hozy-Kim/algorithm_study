# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        def get(l):
            for v in l:
                if v.isInteger():
                    yield v.getInteger()
                else:
                    yield from get(v.getList())
        
        self._generator = get(nestedList)
        self._next_int = next(self._generator, None)
        
    
    def next(self) -> int:
        result = self._next_int
        self._next_int = next(self._generator, None)
        return result
        
    
    def hasNext(self) -> bool:
        return self._next_int is not None
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())