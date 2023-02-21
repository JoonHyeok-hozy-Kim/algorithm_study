
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return
        
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        
        if mid > 0:
            left_child = Solution.sortedArrayToBST(Solution, nums[:mid])
            left_child = self.sortedArrayToBST(nums[:mid])
            node.left = left_child
        if mid < len(nums)-1:
            right_child = self.sortedArrayToBST(nums[mid+1:])
            node.right = right_child
        
        return node
        