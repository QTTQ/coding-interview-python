"""
    p41_find_max_in_sliding_window
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：滑动窗口的最大值

    给定一个数组和滑动窗口大小，找出所有滑动窗口里面的最大值。例如，输入
    数组 [2, 3, 4, 2, 6, 2, 5, 1] 及滑动窗口大小为 3，则最终输出为
    [4, 4, 6, 6, 6, 5]。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from collections import deque
from src.datastructures.stack import Stack


# 实现一个快速获取最大值的栈

class MaxStack(object):
    def __init__(self):
        self._stack = Stack()

    def push(self, x):
        if len(self) == 0:
            maxvalue = x
        else:
            maxvalue = self._top()[-1]
            if x > maxvalue:
                maxvalue = x

        self._stack.push((x, maxvalue))

    def pop(self):
        return self._stack.pop()[0]

    def top(self):
        return self._top()[0]

    def maxvalue(self):
        return self._top()[-1]

    def _top(self):
        tp = self._stack.peek()
        if tp is None:
            return None, None
        return tp

    def __len__(self):
        return len(self._stack)


# 接下来，利用双栈实现一个队列

class MaxQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self._stack_in = MaxStack()
        self._stack_out = MaxStack()

    def __len__(self):
        return len(self._stack_in) + len(self._stack_out)

    def put(self, x):
        # 当队列未满，继续向 stack_in 中添加值
        if not self.full():
            self._stack_in.push(x)

        # 当队列满了后，就把队列头元素弹出，然后追加新的元素
        else:
            _ = self.get()
            self._stack_in.push(x)

    def get(self):
        if len(self._stack_out) == 0:
            while len(self._stack_in) > 0:
                self._stack_out.push(self._stack_in.pop())

        return self._stack_out.pop()

    def maxvalue(self):
        max_in = self._stack_in.maxvalue()
        max_out = self._stack_out.maxvalue()

        if max_in and max_out:
            return max(max_in, max_out)
        return max_in if max_in is not None else max_out

    def full(self):
        return len(self) == self.maxsize


def max_values_of_sliding_window_1(window_size, seq=None):
    """
    这种方案是使用最大值队列来做
    """
    if seq is None:
        return None

    if window_size < 1:
        return None

    if window_size > len(seq):
        return None

    queue = MaxQueue(window_size)
    values = []
    for x in seq:
        queue.put(x)
        if queue.full():
            values.append(queue.maxvalue())

    return values


def max_values_of_sliding_window_2(window_size, seq=None):
    # 采用维护最大值索引的方式来寻找窗口最大值
    # 这里使用 deque 数据结构
    if seq is None:
        return None

    if window_size < 1:
        return None

    if window_size > len(seq):
        return None

    queue = deque()

    # 先初始化滑动窗口
    for i in range(window_size):
        while len(queue) > 0 and seq[i] >= seq[queue[-1]]:
            queue.pop()
        queue.append(i)

    values = []
    # 接下来开始扫描后面的数据，并根据情况抛出小的数值
    for i in range(window_size, len(seq)):
        # 最大值总是在队列最开头
        values.append(seq[queue[0]])

        # 当新数值大于队列尾部数值，则替换
        while len(queue) > 0 and seq[i] >= seq[queue[-1]]:
            queue.pop()

        # 滑出队列中的值
        while len(queue) > 0 and i - queue[0] >= window_size:
            queue.popleft()

        queue.append(i)

    values.append(seq[queue[0]])
    return values


if __name__ == '__main__':
    print(list(max_values_of_sliding_window_2(3, [2, 3, 4, 2, 6, 2, 5, 1])))
