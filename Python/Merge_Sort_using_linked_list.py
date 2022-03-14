from LinkedList import LinkedList


def split(l_list, mid):
    left = LinkedList()
    right = LinkedList()
    left.head = l_list.head
    temp = l_list.address_at_pos(mid-1)
    left.current = temp
    right.head = temp.next
    right.current = l_list.current
    temp.next = None
    return left, right


def merge(left, right):
    l_list = LinkedList()
    left_list = left.head
    right_list = right.head
    while left_list or right_list:
        if right_list is None:
            if l_list.head is None:
                l_list.head = l_list.current = left_list
            else:
                l_list.current.next = left_list

                l_list.current = l_list.current.next
            left_list = left_list.next

        elif left_list is None:
            if l_list.head is None:
                l_list.head = l_list.current = right_list
            else:
                l_list.current.next = right_list
                l_list.current = l_list.current.next
            right_list = right_list.next
        else:
            if left_list.data < right_list.data:
                if l_list.head is None:
                    l_list.head = l_list.current = left_list
                else:
                    l_list.current.next = left_list
                    l_list.current = l_list.current.next
                left_list = left_list.next
            else:
                if l_list.head is None:
                    l_list.head = l_list.current = right_list
                else:
                    l_list.current.next = right_list
                    l_list.current = l_list.current.next
                right_list = right_list.next
    return l_list


def merge_sort(l_list):
    if l_list.head is None or l_list.head.next is None:
        return l_list
    mid = l_list.count()//2
    left, right = split(l_list, mid)
    left = merge_sort(left)
    right = merge_sort(right)
    l_list = merge(left, right)
    return l_list


if __name__ == "__main__":
    l1 = LinkedList()
    n = int(input('Enter #elements :'))
    for i in range(n):
        l1.add_element(int(input('Enter Element :')))
    print(l1)
    l1 = merge_sort(l1)
    print(l1)
