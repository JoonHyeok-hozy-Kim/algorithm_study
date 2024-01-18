# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        curr = root
        def _preorder(node):
            result.append(str(node.val))                

            if node.left:
                result.append('l')
                _preorder(node.left)
            
            if node.right:
                result.append('r')
                _preorder(node.right)
            
            result.append('$')
        
        if root:
            _preorder(root)
        return ''.join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        
        # print(data)
        Q = []
        temp_num = 0
        curr_sign = 'x'
        neg = 1
        result = [None]

        def _num_over(num):
            if curr_sign == '$':
                Q.pop()
            else:
                temp_node = TreeNode(num)
                if curr_sign == 'x':
                    result[0] = temp_node
                elif curr_sign == 'l':
                    Q[-1].left = temp_node
                else:
                    Q[-1].right = temp_node

                Q.append(temp_node)
            

        for s in data:
            # print(result)
            if s.isalpha():
                _num_over(temp_num * neg)
                curr_sign = s
                temp_num = 0
                neg = 1
            elif s.isalnum():
                temp_num *= 10
                temp_num += int(s)
            elif s == '-':
                neg = -1
            else:
                _num_over(temp_num * neg)
                curr_sign = s
                if len(Q) == 0:
                    break
                temp_num = 0
                neg = 1
        
        return result[0]
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))