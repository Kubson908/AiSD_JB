from typing import Any, Callable, List
from graphviz import Graph


class BinaryNode:
    value: Any
    left_child: 'BinaryNode' = None
    right_child: 'BinaryNode' = None

    def __init__(self, value: Any):
        self.value = value

    def is_leaf(self) -> bool:
        if self.left_child is None and self.right_child is None:
            return True
        return False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child is not None:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child is not None:
            self.left_child.traverse_post_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child is not None:
            self.left_child.traverse_pre_order(visit)
        if self.right_child is not None:
            self.right_child.traverse_pre_order(visit)

    def __str__(self) -> Any:
        return str(self.value)


class BinaryTree:
    root: BinaryNode

    def __init__(self, value: Any):
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self):
        graph: Graph = Graph('Binary Tree', filename='binaryTree.gv', format='pdf', engine='dot')

        def add_to_graph(actual_node: BinaryNode):
            if actual_node.left_child is not None:
                graph.edge(str(actual_node), str(actual_node.left_child))
            if actual_node.right_child is not None:
                graph.edge(str(actual_node), str(actual_node.right_child))

        self.traverse_post_order(add_to_graph)
        graph.view()


def right_line(tree: BinaryTree) -> List[BinaryNode]:
    _list: List[BinaryNode] = []
    if tree.root is None:
        return _list

    def append_pre_order_reverse(node: BinaryNode, level: int = 0):
        if len(_list) <= level:
            _list.append(node)
        if node.right_child is not None:
            append_pre_order_reverse(node.right_child, level + 1)
        if node.left_child is not None:
            append_pre_order_reverse(node.left_child, level + 1)

    append_pre_order_reverse(tree.root)
    return _list


tree1 = BinaryTree(10)
tree1.root.add_right_child(2)
tree1.root.right_child.add_right_child(3)
tree1.root.right_child.add_left_child(7)
tree1.root.add_left_child(4)
tree1.root.left_child.add_left_child(1)
tree1.root.left_child.add_right_child(5)
assert tree1.root.value == 10
assert tree1.root.right_child.value == 2
assert tree1.root.right_child.is_leaf() is False
assert tree1.root.left_child.left_child.value == 1
assert tree1.root.left_child.left_child.is_leaf() is True
tree1.show()

li: List[BinaryNode] = right_line(tree1)
for i in li:
    print(i.value)

# tree2: BinaryTree = BinaryTree(3)
# tree2.root.add_right_child(7)
# tree2.root.add_left_child(4)
# tree2.root.right_child.add_right_child(9)
# tree2.root.right_child.right_child.add_right_child(6)
# tree2.root.left_child.add_left_child(1)
# tree2.root.left_child.add_right_child(2)
# tree2.root.left_child.left_child.add_right_child(5)
# tree2.root.left_child.left_child.add_left_child(8)
# tree2.root.left_child.left_child.left_child.add_right_child(0)
# tree2.show()
# li: List[BinaryNode] = right_line(tree2)
# for i in li:
#     print(i.value)
