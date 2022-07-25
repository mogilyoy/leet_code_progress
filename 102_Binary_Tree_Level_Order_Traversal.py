# 102. Binary Tree Level Order Traversal
# Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]

# Example 2:
# Input: root = [1]
# Output: [[1]]

# Example 3:
# Input: root = []
# Output: []

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        node = [root]
        next_layer = []
        node_val = {}
        counter = 0
        if not root:
            return []
        
        while node:
            current = node.pop(0)
            if counter in node_val:
                node_val[counter] += [current.val]
            else:
                node_val[counter] = [current.val]
                
            if current.left:
                next_layer.append(current.left)
        
            if current.right:
                next_layer.append(current.right)
                
                
            if not node:
                node.extend(next_layer)
                next_layer = []
                counter += 1
        return list(node_val.values())
            
            
        




