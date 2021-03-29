class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return str(self.data)

class BinaryTree:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def create_bst(self, nodes_list):
        nodes = [None if item is None else Node(item)
                 for item in nodes_list]

        # root node
        self.__root = nodes[0]

        for index in range(1, len(nodes)):
            node = nodes[index]

            if node is not None:
                parent_index = (index - 1) // 2
                parent = nodes[parent_index]
                if parent is None:
                    raise ValueError(
                        f'Missing parent node at index {parent_index},'
                        f' Node({node.data})')
                if index % 2 == True:
                    parent.left = node
                else:
                    parent.right = node
