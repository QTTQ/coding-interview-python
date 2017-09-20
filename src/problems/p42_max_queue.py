"""
    p42_max_queue
    ~~~~~~~~~~~~~~

    题目：队列的最大值

    定义一个队列并实现函数 max 得到队列里的最大值，要求时间复杂度为 O(1)。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from collections import deque, namedtuple

Element = namedtuple('Element', 'value, index')


class QueueWithMax(object):
    """
    实际上是 p41 思想的应用，类似滑动窗口中找最大值的方式，
    我们同样在这里使用双端队列来存储最大值。
    """

    def __init__(self):
        self._values = deque()
        self._maxvalues = deque()
        self._index = 0

    def put(self, x):
        while len(self._maxvalues) > 0 and x >= self._maxvalues[-1].value:
            self._maxvalues.pop()

        element = Element(x, self._index)
        self._values.append(element)
        self._maxvalues.append(element)
        self._index += 1

    def get(self):
        if self.empty():
            raise IndexError('Queue is empty')

        if self._maxvalues[0].index == self._values[0].index:
            self._maxvalues.popleft()

        return self._values.popleft().value

    @property
    def maxvalue(self):
        if self.empty():
            raise IndexError('Queue is empty')
        return self._maxvalues[0].value

    def __len__(self):
        return len(self._values)

    def empty(self):
        return len(self) == 0
