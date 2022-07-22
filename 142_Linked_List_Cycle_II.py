# 142. Linked List Cycle II
# Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. 
# Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). 
# It is -1 if there is no cycle. Note that pos is not passed as a parameter.
# Do not modify the linked list.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = head
        node_list = {}
        if not lst or not lst.next:
            return
        
        while True:                
            if not lst.next:
                return
            
            elif lst.next not in node_list:
                node_list[lst] = lst.next
                lst = lst.next
            
            else:
                node = lst.next
                break
        pos = 0
        while True:
            if node == lst:
                return node
            
            lst = lst.next
            pos += 1
            

