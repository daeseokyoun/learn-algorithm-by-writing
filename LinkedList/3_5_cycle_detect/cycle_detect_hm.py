from typing import List
import collections

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from linked_list import Node, LinkedList

tests = {
    1: ([3,2,0,4], 1),
    2: ([1, 2], 0),
    3: ([1], -1)
}

res = {
    1: True,
    2: True,
    3: False
}

def create_linked_list(arr):
    l = LinkedList()

    for item in arr:
        l.push_back(item)

    return l

def check_result(index: int, output: bool):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, False) == output

def hasCycle(head: Node) -> bool:
    curr = head
    node_set = set()

    while curr != None:
        if curr in node_set:
            return True

        node_set.add(curr)
        curr = curr.next

    return False

def link_end_to_pos(head: Node, pos):
    cnt = 0
    temp = head
    link_target = None

    while (temp.next):
        if cnt == pos:
            link_target = temp
        temp = temp.next
        cnt += 1

    temp.next = link_target
    return head

def main():
    for index, data in tests.items():
        input_list = data[0]
        pos = data[1]
        l = create_linked_list(input_list)
        cycle_head = l.head
        if pos >= 0:
            cycle_head = link_end_to_pos(l.head, pos)

        output = hasCycle(cycle_head)

        if check_result(index, output):
            print(f'Test case {index} is correct: {output}')
        else:
            print(f'Test case {index} is failed: {output}')

if __name__ == '__main__':
    main()