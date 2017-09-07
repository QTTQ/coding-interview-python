"""
    module queue
    ~~~~~~~~~~~~~~

    FIFO.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


class Queue(object):
    def __init__(self):
        self._elements = []

    def __repr__(self):
        return '<Queue size={!r}>'.format(len(self))

    def enqueue(self, x):
        self._elements.append(x)

    def dequeue(self):
        return self._elements.pop(0)

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._elements)

    def clear(self):
        self._elements.clear()
