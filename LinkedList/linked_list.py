from typing import Any

class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head

        while (temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def push_back(self, data: Any):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    def push(self, data: Any):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        self.head = new_node
        new_node.next = temp

    def remove(self, data: Any):
        curr = self.head
        prev = None

        # head의 요소가 지워지는 요소일 때 처리
        if curr is not None:
            if curr.data == data:
                self.head = curr.next
                curr = None
                return

        while (curr is not None):
            if curr.data == data:
                break
            prev = curr
            curr = curr.next

        # 지우려는 data 노드를 찾지 못했을 때 처리
        if curr == None:
            return

        prev.next = curr.next

        curr = None

    def remove_node(self, node: Node):
        if node == None:
            return

        if node.next == None: 
            return

        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

        next_node = None

