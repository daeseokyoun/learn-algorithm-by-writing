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
    num1_str = ""
    num2_str = ""

    l1_curr = l1
    l2_curr = l2

    while l1_curr != None:
        num1_str = num1_str + str(l1_curr.data)
        l1_curr = l1_curr.next

    while l2_curr != None:
        num2_str = num2_str + str(l2_curr.data)
        l2_curr = l2_curr.next

    res_num = int(num1_str) + int(num2_str)

    # dummy node
    head = Node(-1)
    curr = head
    for num_ch in str(res_num):
        curr.next = Node(int(num_ch))
        curr = curr.next

    curr.next = None
    return head.next

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