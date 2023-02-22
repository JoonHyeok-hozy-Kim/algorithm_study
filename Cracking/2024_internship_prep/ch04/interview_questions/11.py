
class Tree:
    class TreeNode:
        def __init__(self, val, parent=None, left=None, right=None):
            self.val = val
            self.parent = parent
            self.left = left
            self.right = right
    
    def __init__(self):
        self.root = None
        self.size = 0

    def get_root(self):
        return self.root

    def set_root(self, val):
        self.root = self.TreeNode(val)
        self.size += 1
        return self.root
    
    def add_left(self, node, val):
        if node.left:
            raise Exception("left already exists")
        node.left = self.TreeNode(val)
        node.left.parent = node
        self.size += 1
        return node.left
    
    def add_right(self, node, val):
        if node.right:
            raise Exception("right already exists")
        node.right = self.TreeNode(val)
        node.right.parent = node
        self.size += 1
        return node.right
    
    def delete_node(self, node):
        if node.left or node.right:
            raise Exception("Cannot delete a node with child(ren).")
        if node == self.root:
            self.root = None
        else:
            node.parent = None
        self.size -= 1
        return node
    
    def __str__(self):
        from collections import deque
        if self.size > 0:
            Q = deque()
            Q.append([self.root, 0])
            print_level = 0
            while (Q):
                popped = Q[0][0]
                curr_level = Q[0][1]
                if print_level < Q[0][1]:
                    print()
                    print_level += 1
                print(popped.val, end=" ")

                if popped.left:
                    Q.append([popped.left, curr_level+1])
                if popped.right:
                    Q.append([popped.right, curr_level+1])
        print()
                


if __name__ == '__main__':
    t1 = Tree()
    t1.set_root(1)
    t1.add_left(t1.get_root(), 2)
    t1.add_right(t1.get_root(), 3)
    print(t1)