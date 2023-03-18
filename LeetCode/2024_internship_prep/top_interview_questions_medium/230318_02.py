class Solution(object):
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """        
        result_list = []
        num_alpha = [
            0, 0, 'abc',
            'def',
            'ghi',
            'jkl',
            'mno',
            'pqrs',
            'tuv',
            'wxyz',
        ]
        if len(digits) > 0:
            self._recursive(digits, 0, result_list, num_alpha)
        return result_list
        
    def _recursive(self, digits, i, result_list, num_alpha, temp_list=[]):
        if i == len(digits):
            result_list.append(''.join(temp_list))
            return
        
        for c in num_alpha[int(digits[i])]:
            temp_copy = deepcopy(temp_list)
            temp_copy.append(c)
            self._recursive(digits, i+1, result_list, num_alpha, temp_copy)
            