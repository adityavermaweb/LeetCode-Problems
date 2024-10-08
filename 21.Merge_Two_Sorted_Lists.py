# You are given the heads of two sorted linked lists 'list1' and 'list2'.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# Ex:1
# List 1-----> 1    2    3
# List 2-----> 1    3    4

#   1  1  2  3  4  4
# Input : list1 =[1, 2, 4], list2 =[1, 3, 4]
# Output: [1, 1, 2, 3, 4, 4]


# Ex:2
# Input : list1 =[], list2 =[]
# Output : []


# Ex:3
# Input : list1 = [], list2 = [0]
# Output : [0]


# Solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list.val < list2.val:
                cur.next = list1
                list1,cur = list.next,list1
                else:
                    cur.next = list2
                    list2,cur = list2.next,list2
                if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next     