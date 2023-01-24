# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        root3 = TreeNode()

        def treverse(root1, root2, root3):
            if not root1 and not root2:return

            root3.val = root2.val + root1.val
            
            

            if root1.left and root2.left:
                root3.left = TreeNode()
                treverse(root1.left, root2.left, root3.left)
            if root1.right and root2.right:
                root3.right = TreeNode()
                treverse(root1.right, root2.right, root3.right)

            if root1.left and not root2.left:
                root3.left = TreeNode()
                treverse(root1.left, TreeNode(), root3.left)
            if root1.right and not root2.right:
                root3.right = TreeNode()
                treverse(root1.right, TreeNode(), root3.right)

            if not root1.left and root2.left:
                root3.left = TreeNode()
                treverse(TreeNode(), root2.left, root3.left)
            if not root1.right and root2.right:
                root3.right = TreeNode()
                treverse(TreeNode(), root2.right, root3.right)
        
        if not root1:
            return root2
        if not root2:
            return root1

        treverse(root1, root2, root3)
        return root3