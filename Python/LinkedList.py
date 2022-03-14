class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        msg = f'< Node : {self.data}'
        return f'{msg}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def __str__(self):
        temp_list = []
        temp = self.head
        while temp is not None:
            if temp is self.head:
                temp_list.append(f'Head : {self.head.data} ')
            elif temp.next is None:
                temp_list.append(f'Tail : {temp.data}')
            else:
                temp_list.append(f' {temp.data} ')
            temp = temp.next
        return f'{temp_list}'

    def add_element(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.current = new_node

        else:
            self.current.next = new_node
            self.current = self.current.next

    def address_at_pos(self, pos):
        current = self.head
        i = 0
        while i < pos and current.next is not None:
            current = current.next
            i += 1
        return current

    def count(self):
        current = self.head
        cnt = 0
        while current is not None:
            current = current.next
            cnt += 1
        return cnt


if __name__ == "__main__":
    l1 = LinkedList()
    l1.add_element(12)
    l1.add_element(13)
    l1.add_element(15)
    l1.add_element(18)
    l1.add_element(87)
    l1.add_element(64)
    print(l1)
    print(l1.count())
