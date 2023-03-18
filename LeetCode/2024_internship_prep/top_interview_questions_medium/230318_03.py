class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result_list = []
        self._recursive(0, n, result_list)
        return result_list
    
    def _recursive(self, oc, rc, result, temp=[]):
        if oc == 0 and rc == 0:
            result.append(''.join(temp))
            return
        
        if oc > 0:
            temp.append(')')
            self._recursive(oc-1, rc, result, temp)
            temp.pop()
            
        if rc > 0:
            temp.append('(')
            self._recursive(oc+1, rc-1, result, temp)
            temp.pop()