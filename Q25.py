class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Step 1: Append
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node  # Clean one-line assignment
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Step 2: Remove Duplicates using a Set
    def remove_duplicates(self):
        if not self.head: return
        
        seen = set([self.head.data])
        curr = self.head
        
        while curr.next:
            if curr.next.data in seen:
                curr.next = curr.next.next  # Skip the duplicate
            else:
                seen.add(curr.next.data)
                curr = curr.next

    # Step 3: Reverse In-Place
    def reverse(self):
        prev = None
        curr = self.head
        
        while curr:
            nxt = curr.next      # Save next
            curr.next = prev     # Reverse pointer
            prev = curr          # Move prev forward
            curr = nxt           # Move curr forward
            
        self.head = prev         # Set new head

    # Step 4: Print Output
    def print_list(self):
        curr = self.head
        while curr:
            print(curr.data, end=" ")  # Print inline with spaces
            curr = curr.next
        print()


# --- TCS NQT Clean Input Handling ---
if __name__ == "__main__":
    # Assume line 1 is N, line 2 is the elements
    n = int(input())
    elements = list(map(int, input().split()))
    
    ll = LinkedList()
    
    for el in elements:
        ll.append(el)
        
    ll.remove_duplicates()
    ll.reverse()
    ll.print_list()