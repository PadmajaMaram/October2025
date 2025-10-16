# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque,defaultdict
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        d=defaultdict(lambda:defaultdict(list))
        q=deque([(0,0,root)])
        while(len(q)>0):
            vertical,level,node=q.popleft()
            if(node.left):
                q.append((vertical-1,level+1,node.left))
            if(node.right):
                q.append((vertical+1,level+1,node.right))
            d[vertical][level].append(node.val)
        ans=[]
        for i in sorted(d):
            col=[]
            for j in sorted(d[i]):
                col.extend(sorted(d[i][j]))
            ans.append(col)
        return ans
        