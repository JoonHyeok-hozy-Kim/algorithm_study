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
        if root is None:
            return ''
        
        text_list = []
        
        def _inorder(node):
            text_list.append(str(node.val))
            if node.left:
                text_list.append('l');
                _inorder(node.left)
            if node.right:
                text_list.append('r');
                _inorder(node.right)
            text_list.append('_')
        
        _inorder(root)
        return ','.join(text_list)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == '':
            return None
        
        parsed = data.split(',')
        S = [TreeNode(int(parsed[0]))]
        idx = 1
        root = None
        while idx < len(parsed):
            if parsed[idx] == 'l':
                new_node = TreeNode(int(parsed[idx+1]))
                S[-1].left = new_node
                S.append(new_node)
                idx += 2
            elif parsed[idx] == 'r':
                new_node = TreeNode(int(parsed[idx+1]))
                S[-1].right = new_node
                S.append(new_node)
                idx += 2
            elif parsed[idx] == '_':
                root = S.pop()
                idx += 1
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))