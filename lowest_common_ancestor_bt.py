# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def get_path(self, root, n, path):
        if root is None: return None
        
        new_path = path + [root]
        
        if root.val == n.val: return new_path
        
        left_path = self.get_path(root.left, n, new_path)
        right_path = self.get_path(root.right, n, new_path)
        
        if left_path is not None:
            return left_path
        
        if right_path is not None:
            return right_path
        
        return None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.get_path(root, p, [])
        q_path = self.get_path(root, q, [])
        
        lowest_anc = root
        for i in range(1, min(len(p_path), len(q_path))):
            if p_path[i].val == q_path[i].val:
                lowest_anc = q_path[i]
                
        return lowest_anc
        
        
        
        