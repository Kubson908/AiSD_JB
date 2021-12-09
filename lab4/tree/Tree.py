from collections import Callable
from typing import Any, List
from import Queue


class TreeNode:
    value: Any
    children: List['TreeNode']

    def __init__(self, value: Any = None, children = None):
        self.value = value
        self.children = children

    def is_leaf(self) -> bool:
        if self.children is None:
            return True
        else:
            return False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
        for i in self.children:
            i.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        visit(self)
