from typing import List
import collections

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from linked_list import Node, LinkedList

tests = {
    1: ([7,2,4,3], [5,6,4]),
    2: ([7, 8, 2], [2, 1])
}

res = {
    1: [7, 8, 0, 7],
    2: [8, 0, 3]
}

def create_linked_list(arr):
    l = LinkedList()

    for item in arr:
        l.push_back(item)

    return l

def check_result(index:int, head: Node):
    output = []

    temp = head
    while (temp):
        output.append(temp.data)
        temp = temp.next

    return collections.Counter(res.get(index, [])) == collections.Counter(output)

def addTwoNumbers(l1: Node, l2: Node) -> Node:
    st1 = []
    st2 = []

    l1_curr = l1
    l2_curr = l2

    head = None

    while l1_curr != None:
        st1.append(l1_curr.data)
        l1_curr = l1_curr.next

    while l2_curr != None:
        st2.append(l2_curr.data)
        l2_curr = l2_curr.next

    carry = 0
    while st1 or st2:
        num1 = st1.pop() if st1 else 0
        num2 = st2.pop() if st2 else 0

        carry, num = divmod(num1 + num2 + carry, 10)

        node = Node(num)
        if head == None:
            head = node
        else:
            temp = head
            head = node
            node.next = temp

    if carry != 0:
        node = Node(carry)
        temp = head
        head = node
        node.next = temp

    return head


def print_node_list(head: Node):
    if not head:
        return
    temp = head
    while (temp):
        print(f'{temp.data}', end=" ")
        temp = temp.next
    print()

def main():
    for index, data in tests.items():
        l1 = create_linked_list(data[0])
        l2 = create_linked_list(data[1])
        output = addTwoNumbers(l1.head, l2.head)

        if check_result(index, output):
            print(f'Test case {index} is correct:')
            print_node_list(output)
        else:
            print(f'Test case {index} is failed:')

if __name__ == '__main__':
    main()