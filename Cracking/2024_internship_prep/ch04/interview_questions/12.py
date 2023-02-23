class TreeNode:
    def __init__(self, val, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
    
    def __str__(self):
        return "[{}]".format(self.val)
    
    def count_sum_path(self, target: int, curr_sum=0) -> int:
        temp_result = 0
        curr_sum += self.val
        if curr_sum == target:
            temp_result += 1
        print("At {}, curr_sum : {} / temp_result : {}".format(self.val, curr_sum, temp_result))

        if self.left:
            temp_result += self.left.count_sum_path(target, curr_sum)
        if self.right:
            temp_result += self.right.count_sum_path(target, curr_sum)
        
        return temp_result


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(2, t1)
    t1.right = TreeNode(3, t1)
    t1.left.left = TreeNode(7, t1.left)
    t1.left.right = TreeNode(8, t1.left)
    t1.right.left = TreeNode(6, t1.right)
    t1.right.right = TreeNode(7, t1.right)
    t1.left.right.left = TreeNode(-1, t1.left.right)
    t1.left.left.right = TreeNode(-7, t1.left.left)

    print(t1.count_sum_path(3))
    print(t1.count_sum_path(10))