class _Node:
    def __init__(self, key):
        self.key = key

    parent = None
    left_child = None
    right_child = None


class Search_Tree:
    def __init__(self, unsorted_keys=()):
        self.nodes = []

        for key in unsorted_keys:
            self.insert(key)

    def insert(self, key):
        self.nodes.append(_Node(key))

        if len(self.nodes) > 1:
            current_node = self.nodes[0]
            while True:
                assert current_node.key != key
                if key > current_node.key:
                    if current_node.right_child is None:
                        self.nodes.append(_Node(key))
                        self.nodes[-1].parent = current_node
                        current_node.right_child = self.nodes[-1]
                        break

                    else:
                        current_node = current_node.right_child

                else:
                    if current_node.left_child is None:
                        self.nodes.append(_Node(key))
                        self.nodes[-1].parent = current_node
                        current_node.left_child = self.nodes[-1]
                        break

                    else:
                        current_node = current_node.left_child

    def search(self, key, returnNode=False):
        current_node = self.nodes[0]
        while True:
            if current_node.key == key:
                return True if not returnNode else current_node
            if key > current_node.key:
                if current_node.right_child is None:
                    return False

                else:
                    current_node = current_node.right_child

            else:
                if current_node.left_child is None:
                    return False

                else:
                    current_node = current_node.left_child

    def min(self, node=None):
        current_node = self.nodes[0] if node is None else node

        while True:
            if current_node.left_child is None:
                return current_node.key

            else:
                current_node = current_node.left_child

    def max(self, node=None):
        current_node = self.nodes[0] if node is None else node

        while True:
            if current_node.right_child is None:
                return current_node.key

            else:
                current_node = current_node.right_child

    def preceding(self, key):
        node = self.search(key, True)

        if node is False or self.min() == key:
            return False

        if node.left_child is not None:
            return self.max(node.left_child)

        current_node = node.parent

        while True:
            if current_node.key < key:
                return current_node.key

            else:
                current_node = current_node.parent

    def succeeding(self, key):
        node = self.search(key, True)

        if node is False or self.max() == key:
            return False

        if node.right_child is not None:
            return self.min(node.right_child)

        current_node = node.parent

        while True:
            if current_node.key > key:
                return current_node.key

            else:
                current_node = current_node.parent

    def remove(self, key):
        node = self.search(key, True)

        if node is False:
            return False

        if node.left_child is not None and node.right_child is not None:
            new_node = self.preceding(node.key)
            if new_node.parent == node:
                new_node.parent = node.parent
                new_node.right_child = node.right_child
                node.right_child.parent = new_node

                if node.parent.left_child == node:
                    node.parent.left_child = new_node

                else:
                    node.parent.right_child = new_node

            elif new_node.left_child is not None:
                new_node.left_child.parent = new_node.parent
                new_node.parent.right_child = new_node.left_child

                new_node.left_child = node.left_child
                new_node.right_child = node.right_child
                new_node.parent = node.parent

                node.left_child.parent = new_node
                node.right_child.parent = new_node

                if node.parent.left_child == node:
                    node.parent.left_child = new_node

                else:
                    node.parent.right_child = new_node

            else:
                new_node.parent.right_child = None

                new_node.parent = node.parent
                new_node.left_child = node.left_child
                new_node.right_child = node.right_child

                node.left_child.parent = new_node
                node.right_child.parent = new_node

                if node.parent.left_child == node:
                    node.parent.left_child = new_node

                else:
                    node.parent.right_child = new_node

        elif node.right_child is None and node.left_child is not None:
            node.left_child.parent = node.parent

            if node.parent.left_child == node:
                node.parent.left_child = node.left_child

            else:
                node.parent.right_child = node.left_child

        elif node.left_child is None and node.right_child is not None:
            node.right_child.parent = node.parent

            if node.parent.left_child == node:
                node.parent.left_child = node.right_child

            else:
                node.parent.right_child = node.right_child

        else:
            if node.parent.left_child == node:
                node.parent.left_child = None

            else:
                node.parent.right_child = None


if __name__ == "__main__":
    s = Search_Tree([12, 64, 234, 87, 3, 5, 2, 98])
    s.insert(69)
    print(s.search(47))
    print(s.search(64))
    print(s.min())
    print(s.succeeding(87))
    print(s.preceding(234))
    print(s.preceding(3))
    print(s.search(2))
    s.remove(2)
    print(s.search(2))
    print(s.min())
