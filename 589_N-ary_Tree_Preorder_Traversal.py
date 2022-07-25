# 589. N-ary Tree Preorder Traversal
# Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,3,5,6,2,4]


# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root:
            nodes = [root]
            node_vals = []
            while nodes:
                current = nodes.pop()
                node_vals.append(current.val)
                a = current.children
                if a:
                    a.reverse()
                    for node in a:
                        nodes.append(node)
                else:
                    continue
            return node_vals
            