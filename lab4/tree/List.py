from typing import Any
from List import Queue

# ZADANIE 1
class Node:
    value: Any
    next: 'Node'

    def __init__(self, value=None, next2=None):
        self.value = value
        self.next = next2


class LinkedList:
    head: Node
    tail: Node

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __str__(self) -> str:
        if self.head is None:
            return str(None)
        s: str = ""
        temp: Node = self.head
        s += str(temp.value)
        while temp is not self.tail:
            temp = temp.next
            s += (" -> " + str(temp.value))
        return s

    def __len__(self) -> int:
        if self.head is None:
            return 0
        temp: Node = self.head
        length: int = 1
        while temp is not self.tail:
            temp = temp.next
            length += 1
        return length

    def push(self, value: Any) -> None:
        node2: Node = Node(value)
        if self.head is not None:
            node2.next = self.head
            self.head = node2
        else:
            self.head = node2
            self.tail = node2

    def append(self, value: Any) -> None:
        node2: Node = Node(value)
        if self.tail is not None:
            self.tail.next = node2
            self.tail = node2
        else:
            self.head = node2
            self.tail = node2

    def node(self, at: int) -> Node:
        temp: Node = self.head
        if self.head is None:
            return temp
        for i in range(at):
            temp = temp.next
            if temp.next is None:
                break
        return temp

    def insert(self, value: Any, after: Node) -> None:
        temp: Node = self.head
        node2: Node = Node(value)
        while temp is not None:
            if temp == after:
                node2.next = temp.next
                temp.next = node2
                break
            temp = temp.next

    def pop(self) -> Any:
        temp: Node = self.head
        self.head = self.head.next
        return temp.value

    def remove_last(self) -> Any:
        last: Node = self.tail
        temp: Node = self.head
        while temp.next is not last:
            temp = temp.next
        self.tail = temp
        return last.value

    def remove(self, after: Node) -> Any:
        temp: Node = self.head
        if after == self.tail:
            return None
        while temp is not None:
            if after.next == self.tail:
                self.tail = after
            if temp == after:
                temp.next = temp.next.next
                return after.next.value
            temp = temp.next


li = LinkedList()
assert li.head is None
li.push(1)
li.push(0)
assert str(li) == '0 -> 1'
li.append(9)
li.append(10)
assert str(li) == '0 -> 1 -> 9 -> 10'
middle_node = li.node(at=1)
li.insert(5, after=middle_node)
assert str(li) == '0 -> 1 -> 5 -> 9 -> 10'
first_element = li.node(at=0)
returned_first_element = li.pop()
assert first_element.value == returned_first_element
last_element = li.node(at=3)
returned_last_element = li.remove_last()
assert last_element.value == returned_last_element
assert str(li) == '1 -> 5 -> 9'
second_node = li.node(at=1)
li.remove(second_node)
assert str(li) == '1 -> 5'


# ZADANIE 2
class Stack:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __str__(self) -> str:
        if self._storage.head is None:
            return str(None)
        temp: LinkedList = LinkedList()
        temp2: Node = self._storage.head
        s: str = ""
        s2: str = s
        temp.push(self._storage.head.value)
        while temp2 is not self._storage.tail:
            s = (str(temp.tail.value) + "\n" + s2)
            s2 = s
            temp2 = temp2.next
            temp.append(temp2.value)
        s = (str(temp.tail.value) + "\n" + s2)
        return s

    def __len__(self) -> int:
        return len(self._storage)

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self) -> Any:
        return self._storage.remove_last()


stack = Stack()
assert len(stack) == 0
stack.push(3)
stack.push(10)
stack.push(1)
assert len(stack) == 3
top_value = stack.pop()
assert top_value == 1
assert len(stack) == 2


# ZADANIE 3
class Queue:
    _storage: LinkedList

    def __init__(self):
        self._storage = LinkedList()

    def __str__(self):
        if self._storage.head is None:
            return str(None)
        s: str = ""
        temp: Node = self._storage.head
        s += str(temp.value)
        while temp is not self._storage.tail:
            temp = temp.next
            s += (", " + str(temp.value))
        return s

    def __len__(self) -> int:
        return len(self._storage)

    def peek(self) -> Any:
        return self._storage.head.value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()


queue = Queue()
assert len(queue) == 0
queue.enqueue('klient1')
queue.enqueue('klient2')
queue.enqueue('klient3')
assert str(queue) == 'klient1, klient2, klient3'
client_first = queue.dequeue()
assert client_first == 'klient1'
assert str(queue) == 'klient2, klient3'
assert len(queue) == 2
