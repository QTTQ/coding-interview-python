"""
    p19_remove_duplicate_nodes_from_list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：删除链表中重复的节点

    在一个排序的链表中，如何删除重复的节点？
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.datastructures.linkedlist.single import List


def remove_duplicates(data):
    if data is None:
        return None

    if len(data) == 0:
        return []

    head = List.fromvalues(data).head
    return list(List.fromhead(_remove_duplicates(head)))


def _remove_duplicates(head):
    """
    考虑到这是一个有序的链表，我们可以设置两个指针 p, q，一个在前一个在后
    1. 当 p.val == q.val 时，则删除节点 q，然后 q = p.next
    2. 当 p.val != q.val 时，则 p = p.next, q = q.next

    重复上述过程，直到 q 移动到最后一个节点为止
    """
    if head is None:
        return None

    p = head.next

    # 如果没有节点则退出
    if p is None:
        return head

    q = p.next
    # 如果节点数不超过一个，则退出
    if q is None:
        return head

    # 到这儿，意味着至少存在两个非空节点了
    # 直到 q 到最后一个节点为止
    while q.next is not None:
        if p.val != q.val:
            p = p.next
            q = q.next
        else:
            old = q
            p.next = q.next
            q = q.next
            del old

    # 此时，如果两个节点相等，则移除 q 即可
    if p.val == q.val:
        p.next = None
        del q

    return head
