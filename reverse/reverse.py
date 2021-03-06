class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev): # Tests start from head, prev = None
        # self.next_node = node.next_node
        # node.next_node = prev
        # if self.next_node is None:
        #     return node
        # else:
        #     return self.reverse_list(self.next_node, node)


        if node is not None: # 2
            next = node.next_node # 3
            node.next_node = prev # 1
            prev = node # 2
            node = next # 3
            self.reverse_list(node, prev)
        else:
            self.head = prev
            return

        # iteratively
        while node is not None:
            next = node.next_node
            node.next_node = prev
            prev = node
            node = next
        self.head = prev
