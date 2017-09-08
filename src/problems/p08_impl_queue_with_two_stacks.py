"""
    p08_impl_queue_with_two_stacks
    ~~~~~~~~~~~~~~

    题目：用两个栈实现一个队列

    要求实现队列的两个方法：`append_tail` 和 `pop_head`。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.datastructures.stack import Stack


class Queue(object):
    """个人思路：
    将 stack_a 作为核心队列容器，所有元素必须入这个栈中
    将 stack_b 作为临时交换容器，用于换出"队列"中的先头
    元素
    """

    def __init__(self):
        self._stack_a = Stack()
        self._stack_b = Stack()

    def __len__(self):
        return len(self._stack_a) + len(self._stack_b)

    def append_tail(self, x):
        # 所有的新元素都放在 a 中
        self._stack_a.push(x)

    def pop_head(self):
        # 当 stack_b 为空时，我们将 stack_a 中的元素转移到 b 中，
        # 这样元素的顺序在 stack_b 中就变为原来的逆序，然后从 b 中
        # 弹出元素，即为队列的头元素
        if len(self) == 0:
            raise RuntimeError('The queue is empty')

        if len(self._stack_b) == 0:
            self._populate_stack_b()

        return self._stack_b.pop()

    def _populate_stack_b(self):
        while len(self._stack_a) >= 1:
            self._stack_b.push(self._stack_a.pop())
