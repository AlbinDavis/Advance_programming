# Given a singly linked list, delete middle of the linked list. For example, if given linked list is 1->2->3->4->5 then linked list should be modified to 1->2->4->5.
# If there are even nodes, then there would be two middle nodes, we need to delete the second middle element. For example, if given linked list is 1->2->3->4->5->6 then it should be modified to 1->2->3->5->6.
# If the input linked list is NULL or has 1 node, then it should return NULL

# Example 1:

# Input:
# LinkedList: 1->2->3->4->5
# Output: 1 2 4 5

def deleteMid(head):
    if head is None:
        return None
    
    slow=head
    fast=head
    while fast != None and fast.next!=None:
        prev=slow
        slow=slow.next
        fast=fast.next.next
    prev.next=slow.next
    return head
