# 92. Reverse Linked List II
# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, 
# and return the reversed list.
# Example 1:
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]

# Example 2:
# Input: head = [5], left = 1, right = 1
# Output: [5]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
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
            b = a[left-1:right]
            b.reverse()
            a = a[:left-1] + b + a[right:]            
            for i in a:
                new_node = ListNode(val=i)  
                new_list.next = new_node
                new_list = new_list.next
            return heading.next
# Взял то же самое решение что и в 206_Reverse_Linked_List.py, только изменил массив а. Думаю, не самое лаконичное решение, но пока лучше не умею

