"""
    module deque
    ~~~~~~~~~~~~~~

    A special queue: double-ended queue.

    However, `collections.deque` may be a better choice if you want to add a
    double-ended queue in your production code.

    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


class Deque(object):
    def __init__(self):
        self._elements = []

    def __repr__(self):
        return '<Deque size={!r}>'.format(len(self))

    def append_front(self, x):
        self._elements.insert(0, x)

    def pop_front(self):
        return self._elements.pop(0)

    def append_rear(self, x):
        self._elements.append(x)

    def pop_rear(self):
        return self._elements.pop()

    def __len__(self):
        return len(self._elements)

    def is_empty(self):
        return len(self) == 0

    def clear(self):
        self._elements.clear()
