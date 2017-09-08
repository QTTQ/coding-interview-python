"""
    p09_impl_stack_with_two_queues
    ~~~~~~~~~~~~~~

    题目：使用两个队列实现一个栈

    要求实现一个栈，使用两个队列模拟栈的操作，实现 `pop` 和 `push` 方法
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


class Stack(object):
    def __init__(self):
        # 为简单起见，使用两个 `list` 容器模拟队列的操作
        self._queue_a = list()
        self._queue_b = list()

    def __len__(self):
        return len(self._queue_a) + len(self._queue_b)

    def push(self, x):
        if len(self) == 0 or len(self._queue_a) > 0:
            self._queue_a.append(x)
        else:
            self._queue_b.append(x)

    def pop(self):
        if len(self) == 0:
            raise RuntimeError('The stack is empty')

        # 将空队列作为保存弹出的元素存储区
        from_queue = self._queue_a if len(self._queue_a) > 0 else self._queue_b
        to_queue = self._queue_a if len(self._queue_a) == 0 else self._queue_b
        self._transfer_elements(from_queue, to_queue)

        return from_queue.pop(0)

    @staticmethod
    def _transfer_elements(from_, to):
        while len(from_) > 1:
            to.append(from_.pop(0))


if __name__ == '__main__':
    pass
