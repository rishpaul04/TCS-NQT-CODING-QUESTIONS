# Problem Statement
# You are given an input consisting of an integer N (number of elements) followed by N integers.
# You need to perform the following operations in order:

# Create a linked list from the input elements.

# Remove duplicate nodes, keeping only the first occurrence of each element.

# Reverse the linked list.

# Print the reversed linked list as space-separated values.

import sys
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
    def remove_duplicates(self):
        current=self.head
        prev=None
        seen=set()
        while current:
            if current.data in seen:
                prev.next=current.next
            else:
                seen.add(current.data)
                prev=current
            current=current.next
    def reverse(self):
        prev=None
        current=self.head
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        self.head=prev
    def print_list(self):
        current=self.head
        result=[]
        while current:
            result.append(str(current.data))
            current=current.next
        print(" ".join(result))