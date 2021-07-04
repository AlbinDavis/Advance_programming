# Given a linked list of N nodes. The task is to reverse this list.

# Example 1:

# Input:
# LinkedList: 1->2->3->4->5->6
# Output: 6 5 4 3 2 1
# Explanation: After reversing the list, 
# elements are 6->5->4->3->2->1.

class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        temp=head.next
        head.next=None

        while temp!=None:
            temp2=temp
            temp=temp.next
            temp2.next=head
            head=temp2
        return head
