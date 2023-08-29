class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = None

    def printl(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def append(self, data):

        new_node = Node(data)
        print(new_node)
        if not self.head:
            self.head = new_node  # adding address of new node to head as it is the fist node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        # adding address of next node to previous node while maintaining last position
        last_node.next = new_node


ll = linkedlist()
ll.append('Aasdas')
ll.append('Hasdas')
ll.append('Apoorv')
ll.printl()
