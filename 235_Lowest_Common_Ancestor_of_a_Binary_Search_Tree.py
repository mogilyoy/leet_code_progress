# 235. Lowest Common Ancestor of a Binary Search Tree
# Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def search_path(root, number, path = []):
    if not isinstance(number, int):
        if root.val == number.val:
            path.append(root.val)
            return path

        if number.val < root.val and root.left != None:  
            path.append(root.val)
            return search_path(root.left, number, path)

        if number.val > root.val and root.right != None:
            path.append(root.val)
            return search_path(root.right, number, path)

        return -1
    else: 
        if root.val == number:
            return root

        if number < root.val and root.left != None:  
            return search_path(root.left, number, path)

        if number > root.val and root.right != None:
            return search_path(root.right, number, path)

        return -1


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        path_p = search_path(root, p, path = [])
        path_q = search_path(root, q, path = [])
        for i in path_p[::-1]:
            if i in path_q:
                parent_val = i
                break
        return search_path(root, parent_val, path = [])
