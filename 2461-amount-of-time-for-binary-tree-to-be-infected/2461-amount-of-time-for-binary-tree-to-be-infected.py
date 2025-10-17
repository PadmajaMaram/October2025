# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def amountOfTime(self, root, start):
        """
        :type root: Optional[TreeNode]
        :type start: int
        :rtype: int
        """
        def get_parent(root):
            q=deque([root])
            mpp={}
            while(q):
                node=q.popleft()
                if(node.left):
                    q.append(node.left)
                    mpp[node.left]=node
                if(node.right):
                    q.append(node.right)
                    mpp[node.right]=node
            return mpp
        def preorder(root,start):
            if(root==None):
                return None
            if(root.val==start):
                return root
            path1=preorder(root.left,start)
            if(path1!=None):
                return path1
            path2=preorder(root.right,start)
            return path1 or path2
        parent=get_parent(root)
        startnode_address=preorder(root,start)
        vis=set([startnode_address])
        q=deque([startnode_address])
        m=0
        while(len(q)>0):
            for i in range(len(q)):
                node=q.popleft()
                if(node in parent and parent[node] not in vis):
                    vis.add(parent[node])
                    q.append(parent[node])
                if(node.left and node.left not in vis):
                    vis.add(node.left)
                    q.append(node.left)
                if(node.right and node.right not in vis):
                    vis.add(node.right)
                    q.append(node.right)
            m+=1
        return m-1


