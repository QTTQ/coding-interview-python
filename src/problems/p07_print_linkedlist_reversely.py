"""
    p07_print_linkedlist_reversely
    ~~~~~~~~~~~~~~

    输入一个链表的头节点，从尾到头打印出每个节点的值
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def visit_linkedlist_reversely1(head):
    """第一种方法就是使用递归的方式打印，利用栈的 FILO 特点很容易实现"""
    if head is None:
        return None

    visit_linkedlist_reversely1(head.next)
    print(head.val, end=' ')


def visit_linkedlist_reversely2(head):
    """利用一个栈结构存储节点，避免递归深度过大导致可能的栈溢出问题，提高
    程序的鲁棒性"""
    if head is None:
        return None

    from collections import deque
    nodes = deque()

    while head is not None:
        nodes.append(head.val)
        head = head.next

    while len(nodes) > 0:
        print(nodes.pop(), end=' ')


if __name__ == '__main__':
    from src.datastructures.linkedlist.single import List

    l = List.fromvalues([1, 2, 3, 4])
    visit_linkedlist_reversely1(l.head.next)
    visit_linkedlist_reversely2(l.head.next)
