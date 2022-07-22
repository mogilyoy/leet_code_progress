# 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.

# Example 2:
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new_list = ListNode()
        heading = new_list
        if head:
            a = [head.val]
            while True:
                if head.next:
                    a.append(head.next.val)
                    head = head.next
                else: 
                    break
            a = a[len(a)//2:]
            for i in a:
                new_node = ListNode(val=i)  
                new_list.next = new_node
                new_list = new_list.next
            return heading.next
        
 