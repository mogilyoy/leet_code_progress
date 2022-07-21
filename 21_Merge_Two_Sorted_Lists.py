# 21. Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        new_list = ListNode()
        head = new_list
        inf = float('inf')
        if list1 and not list2:
            return list1
        elif not list1 and list2:
            return list2
        elif not list1 and not list2:
            return 
        
        while True:
            if list1.val == inf and list2.val == inf: 
                break

            new_node = ListNode()
            if list1.val > list2.val:
                new_node.val = list2.val                    
                while new_list.next:
                    new_list = new_list.next
                new_list.next = new_node                
                if list2.next:
                    list2 = list2.next
                else:
                    list2.val = inf

            elif list1.val <= list2.val:    
                new_node.val = list1.val               
                while new_list.next:
                    new_list = new_list.next
                new_list.next = new_node
                if list1.next:
                    list1 = list1.next
                else:
                    list1.val = inf
                    
        return head.next        
# Заплатка на заплатке, но я пока очень мало знаком с такими структурами


