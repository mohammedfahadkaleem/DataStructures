class Node:
    def __init__(self,data=None, next_node=None, previous_node=None):
        self.data = data
        self.nextNode = next_node
        self.previousNode = previous_node

    def set_data(self,data):
         self.data = data

    def get_data(self):
         return self.data

    def set_nextNode(self,nextNode):
         self.nextNode = nextNode

    def get_nextNode(self):
         return self.nextNode

    def set_previousNode(self,previousNode):
         self.previousNode = previousNode

    def get_previousNode(self):
         return self.previousNode


class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.length = 0


