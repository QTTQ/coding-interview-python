"""
    p26_min_stack
    ~~~~~~~~~~~~~~

    问题：包含 min 函数的栈

    定义栈的数据结构，在该类型中实现一个能够得到栈最小元素的 min 函数，
    且调用 min, push, pop 的时间复杂度均为 O(1)

    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from collections import deque, namedtuple

Element = namedtuple('Element', 'val, min')


class Stack(object):
    def __init__(self):
        self._elements = deque()

    def empty(self):
        return len(self._elements) == 0

    def pop(self):
        if not self.empty():
            return self._elements.pop().val

    def push(self, x):
        if self.empty():
            e = Element(x, x)
        else:
            min_val = x if x < self.min() else self.min()
            e = Element(x, min_val)
        self._elements.append(e)

    def min(self):
        return self._top().min

    def top(self):
        return self._top().val

    def _top(self):
        if not self.empty():
            return self._elements[-1]

        return Element(None, None)


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(0)
    print(s.min())
    s.push(-1)
    print(s.min())
    s.pop()
    print(s.min())
    s.pop()
    print(s.min())
    s.pop()
    print(s.min())
