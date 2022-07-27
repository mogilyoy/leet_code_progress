# 98. Validate Binary Search Tree
# Given the root of a binary tree, determine if it is a valid binary search tree (BST).
# A valid BST is defined as follows:
#     The left subtree of a node contains only nodes with keys less than the node's key.
#     The right subtree of a node contains only nodes with keys greater than the node's key.
#     Both the left and right subtrees must also be binary search trees.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        values = []
        queue = [root]
        
        while queue:
                current = queue.pop()
                if current.left:
                        if current.left.val >= current.val:
                                        return False
                        queue.append(current)
                        queue.append(current.left)
                        current.left = None
                        continue
                else:
                        if current.right:
                                if current.right.val <= current.val:
                                        return False
                                
                                values.append(current.val)
                                queue.append(current.right)
                                continue
                        else:
                                values.append(current.val)
                                continue
                                     
        if values == sorted(list(set(values))):
                return True
        return False