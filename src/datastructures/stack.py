"""
    module stack
    ~~~~~~~~~~~~~~

    Stack data structure.
    LIFO
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


class _Stack(object):
    container = None

    def __init__(self):
        self._elements = self.container()

    def __repr__(self):
        return '<Stack size={!r}>'.format(len(self))

    def push(self, x):
        self._elements.append(x)

    def pop(self):
        return self._elements.pop()

    def peek(self):
        if len(self) > 0:
            return self._elements[-1]

    def clear(self):
        self._elements.clear()

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._elements)


class ListStack(_Stack):
    """
    Implement the stack interfaces with a builtin `list`.
    """
    container = list


class DequeStack(_Stack):
    """
    Implement the stack interfaces with a `deque` container.
    `deque` is optimized for operations on its both ends.
    See `https://docs.python.org/2/library/collections.html` for details.
    """
    from collections import deque
    container = deque


# `DequeStack` as the default implementation
Stack = DequeStack

__all__ = ['Stack', 'ListStack', 'DequeStack']
