class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next

n=int(input("Enter the limit:"))

for i in range(n):
    if i == 0:
        llist=Linkedlist()
        print("Enter node 1 data")
        s=input()
        llist.head=node(s)
        temp=llist.head
    else:
        print("Enter node",i+1, "data")
        s=input()
        ob=node(s)
        temp.next=ob
        temp=ob
llist.printlist()


