# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def get(root):
            a=[]
            def dfs(node):
                if not node:
                    return 
                if not node.left and not node.right:
                    a.append(node.val)
                    return 
                dfs(node.left)
                dfs(node.right)
            dfs(root)
            return a
        return get(root1)==get(root2)
        