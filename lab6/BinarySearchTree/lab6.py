import time
from typing import Any, List, Callable
from graphviz import Graph


class BinaryNode:
    value: Any
    left_child: 'BinaryNode' = None
    right_child: 'BinaryNode' = None

    def __init__(self, value: Any):
        self.value = value

    def min(self) -> 'BinaryNode':
        if self.left_child is not None:
            return self.left_child.min()
        return self

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def is_leaf(self) -> bool:
        if self.left_child is None and self.right_child is None:
            return True
        return False


class BinarySearchTree:
    root: BinaryNode

    def __init__(self, value: Any):
        self.root = BinaryNode(value)

    def insert(self, value: Any) -> None:
        self._insert(self.root, value)

    def _insert(self, node: BinaryNode, value: Any) -> BinaryNode:
        if node is None:
            node = BinaryNode(value)
            return node
        if value < node.value:
            node.left_child = self._insert(node.left_child, value)
        elif value >= node.value:
            node.right_child = self._insert(node.right_child, value)
        return node

    def insertlist(self, list: List[Any]) -> None:
        for i in list:
            self.insert(i)

    def contains(self, value: Any) -> bool:
        temp_node: BinaryNode = self.root
        while temp_node is not None:
            if value == temp_node.value:
                return True
            if value < temp_node.value:
                temp_node = temp_node.left_child
            else:
                temp_node = temp_node.right_child

        return False

    def remove(self, value: Any):
        self._remove(self.root, value)

    def _remove(self, node: BinaryNode, value: Any):
        if value == node.value:
            if node.is_leaf():
                return None
            if node.left_child is None:
                return node.right_child
            if node.right_child is None:
                return node.left_child
            min_val = node.right_child.min().value
            node.value = min_val
            node.right_child = self._remove(node.right_child, min_val)
        if value < node.value and node.left_child is not None:
            node.left_child = self._remove(node.left_child, value)
        if value > node.value and node.right_child is not None:
            node.right_child = self._remove(node.right_child, value)
        return node

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def show(self):
        graph: Graph = Graph('Binary Search Tree', filename='BST.gv', format='pdf', engine='dot')

        def add_to_graph(actual_node: BinaryNode):
            if actual_node.left_child is not None:
                graph.edge(str(actual_node.value), str(actual_node.left_child.value))
            if actual_node.right_child is not None:
                graph.edge(str(actual_node.value), str(actual_node.right_child.value))

        self.traverse_post_order(add_to_graph)
        graph.view()
        

tree: BinarySearchTree = BinarySearchTree(7)
tree.insertlist([3, 1, 5, 15, 9, 11, 8, 6, 2, 0, 19, 17, 22, 4])
tree.show()
time.sleep(2)
tree.remove(3)
tree.show()
