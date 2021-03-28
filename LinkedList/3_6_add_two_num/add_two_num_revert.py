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
    def reverse(head):
        prev = None
        curr = head

        while curr != None:
            next_temp = curr.next
            curr.next = prev

            prev = curr
            curr = next_temp
        return prev

    r_l1 = reverse(l1)
    r_l2 = reverse(l2)

    res_head = None

    carry = 0
    while r_l1 != None or r_l2 != None:
        num1 = 0
        num2 = 0

        if r_l1 != None:
            num1 = r_l1.data
            r_l1 = r_l1.next
        if r_l2 != None:
            num2 = r_l2.data
            r_l2 = r_l2.next

        carry, num = divmod(num1 + num2 + carry, 10)

        node = Node(num)
        if res_head == None:
            res_head = node
        else:
            temp = res_head
            res_head = node
            node.next = temp

    if carry != 0:
        node = Node(carry)
        temp = res_head
        res_head = node
        node.next = temp

    return res_head


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