# 429. N-ary Tree Level Order Traversal
# Given an n-ary tree, return the level order traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        queue = [root]
        queue_next = []
        res = []
        cur_res = []
    
        if not root:
            return
        
        while True: 
            current = queue.pop(0)
            cur_res.append(current.val)
            
            if current.children:
                queue_next.extend(current.children)
                  
            if not queue and queue_next:
                queue.extend(queue_next)
                res.append(cur_res)
                cur_res = []
                queue_next = []
                
            if not queue and not queue_next:
                queue.extend(queue_next)
                res.append(cur_res)
                break
                
        return res
