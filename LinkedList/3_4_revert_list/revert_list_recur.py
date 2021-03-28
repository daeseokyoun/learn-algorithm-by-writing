from typing import List
import collections

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from linked_list import Node, LinkedList

tests = {
    1: [1,2,3,4,5],
    2: [1, 2],
    3: []
}

res = {
    1: [5,4,3,2,1],
    2: [1, 2],
    3: [],
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

def reverseList(head: Node) -> Node:
    if head == None or head.next == None:
        return head

    reversed_list = reverseList(head.next)
    head.next.next = head
    head.next = None

    return reversed_list

def print_node_list(head: Node):
    if not head:
        return
    temp = head
    while (temp):
        print(f'{temp.data}', end=" ")
        temp = temp.next
    print()

def main():
    for index, input_list in tests.items():
        l = create_linked_list(input_list)
        output = reverseList(l.head)

        if check_result(index, output):
            print(f'Test case {index} is correct:')
            print_node_list(output)
        else:
            print(f'Test case {index} is failed:')

if __name__ == '__main__':
    main()