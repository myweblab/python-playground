
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self,next):
        if(self.head==None):
            self.head = next
        else:
            self.head.next = next
    
    @property
    def current(self):
        return self.head
    
    @current.setter
    def current(self,node):
        self.head = node

    
    def show(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next

    def remove(self,node):
        curr = self.head
        if(curr == node):
            self.head = curr.next
        else:
            while curr.next!=node or curr.next is None:
                curr = curr.next
            if(curr.next is not None):
                   curr.next = curr.next.next

import argparse
if(__name__=="__main__"):
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",help="", type=int)
    args = parser.parse_known_args()
    l = LinkedList()
    l.head = Node("Test")
    s = Node("This")
    l.add(s)
    l.show()
    l.remove(s)
    l.show()
    print(l.current)
    l.current = s
    l.show()
