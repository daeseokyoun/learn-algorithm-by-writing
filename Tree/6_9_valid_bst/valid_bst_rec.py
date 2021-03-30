import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from collections import deque
import collections
from typing import List

from binarytree import BinaryTree, Node

tests = {
    1: [5,1,4,'N','N',3,6],
    2: [2,1,3],
    3: [8,6,15,3,7,12,21],
    4: [1, 1],
    5: [8,5,15,6,7,12,21]
}

res = {
    1: False,
    2: True,
    3: True,
    4: False,
    5: False
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

def check_result(index: int, output: int):
    if index > len(tests):
        raise RuntimeError(f'Failed to get {index}th case')
    return res.get(index, False) == output

def isValidBST(root: Node) -> bool:
    low = float('-inf')
    high = float('inf')

    def isValidBSTRec(node: Node, low: int,
                      high: int) -> bool:
        if node == None:
            return True

        if node.data <= low or node.data >= high:
            return False

        return isValidBSTRec(node.left, low, node.data)\
          and isValidBSTRec(node.right, node.data, high)

    return isValidBSTRec(root, low, high)

def main():
    for index, tree_input in tests.items():
        bst = parse_tree(tree_input)
        res = isValidBST(bst.root)

        if check_result(index, res):
            print(f'Test case {index} is correct: {res}')
        else:
            print(f'Test case {index} is failed: {res}')

if __name__ == '__main__':
    main()
