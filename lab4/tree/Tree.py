from typing import Any, List, Union, Callable
from List import Queue


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any = None):
        self.value = value

    def is_leaf(self) -> bool:
        if self.children is None:
            return True
        return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for i in self.children:
            i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        queue: Queue = Queue()
        for i in self.children:
            queue.enqueue(i)
        while len(queue) > 0:
            visit(queue.enqueue())
            for i in self.children:
                queue.enqueue(i)

    # def search(self, value: Any) -> Union['TreeNode', None]:

    def __str__(self) -> Any:
        return self.value


class Tree:
    root: TreeNode

    def __init__(self, root: TreeNode):
        self.root = root

    def add(self, value: Any, parent_name: Any):
        parent_name.add(value)

