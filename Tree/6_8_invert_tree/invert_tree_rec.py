import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from collections import deque
import collections
from typing import List

from binarytree import BinaryTree, Node

tests = {
    1: [4,2,7,1,3,6,9],
    2: [2,1,3],
    3: []
}

res = {
    1: [4,7,2,9,6,3,1],
    2: [2,3,1],
    3: []
}

def parse_tree(tree_input):
    bst = BinaryTree()

    if not tree_input:
        return bst

    input_datas = []
    for item in tree_input:
        if item == 'N':
            input_datas.append(None)
        else:
            input_datas.append(int(item))

    bst.create_bst(input_datas)
    return bst

def is_same_list(alist: List, blist: List):
    return collections.Counter(alist) == collections.Counter(blist)

def check_result(index: int, output: List):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')

    return is_same_list(output, res.get(index, []))

def invertTree(root: Node) -> Node:
    if root == None:
        return None

    left = root.left
    root.left = root.right
    root.right = left

    invertTree(root.left)
    invertTree(root.right)

    return root

def main():
    for index, tree_input in tests.items():
        bst = parse_tree(tree_input)
        node_head = invertTree(bst.root)

        res = bst.inorder_traverse(node_head)
        if check_result(index, res):
            print(f'Test case {index} is correct')
        else:
            print(f'Test case {index} is failed')

if __name__ == '__main__':
    main()
