"""
    p23_reverse_list
    ~~~~~~~~~~~~~~

    问题：链表反转

    定义一个函数，输入一个链表的头节点，反转该链表并输出反转后的链表。

    个人喜欢假设有一个空的头节点，然后后面跟随着所有的节点，所以所有的
    链表相关题都假设有这个空的头节点咯。

    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""
from functools import wraps

from src.datastructures.linkedlist.single import List


def to_pylist(func):
    @wraps(func)
    def _(*args, **kwargs):
        head = func(*args, **kwargs)
        if head is not None:
            return list(List.fromhead(head))
        return None

    return _


@to_pylist
def reverse_list(values):
    if values is None:
        return None

    if len(values) == 0:
        return None

    head = List.fromvalues(values).head

    p = head.next
    # 只有一个节点的情况
    if p.next is None:
        return head

    # 此时至少有了两个节点
    q = p.next

    # 断开 p 节点与下一个节点的连接
    p.next = None

    while q:
        next_node = q.next
        q.next = p
        p = q
        q = next_node

    # 此时的尾部节点就是 p
    head.next = p
    return head


if __name__ == '__main__':
    print(reverse_list([1]))
