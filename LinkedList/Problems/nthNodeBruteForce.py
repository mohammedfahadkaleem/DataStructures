"""
Author: Mohammed Fahad Kaleem
"""

class Node:
    def __init__(self,data,next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data

    def get_next_node(self):
        return self.next_node

    def set_next_node(self,next_node):
        self.next_node = next_node


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self,data):
        new_node = Node(data)
        if self.length==0:
            self.head = new_node
            self.length += 1
        else:
            current_node = self.head
            while current_node:
                current_node = current_node.get_next_node()
            current_node.set_next_node(new_node)
            self.length += 1

    def nth_node(self,n):
        if self.length < n:
            print("Value of n is greater than the length of the linked list")
            return False
        else:
            current_node = self.head
            nth_node = self.length - n + 1
            for i in range(nth_node):
                current_node = current_node.get_next_node
            return current_node.get_data()



if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(12)
    linked_list.insert(16)
    linked_list.insert(3)
    linked_list.insert(15)
    linked_list.nth_node(2)

