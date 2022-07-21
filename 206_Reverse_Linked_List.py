# 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

        
class Solution(object):
    def reverseList(self, head):
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
            a.reverse()
            for i in a:
                new_node = ListNode(val=i)  
                new_list.next = new_node
                new_list = new_list.next
            return heading.next