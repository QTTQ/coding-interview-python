"""
    p18_delete_node_from_list
    ~~~~~~~~~~~~~~~~~~~~~~~~

    题目：删除链表的节点

    给定单向链表的头指针和一个节点指针，定义一个函数在 O(1) 时间内删除
    该节点。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.datastructures.linkedlist.single import List


def delete(data, val):
    if data is None:
        return None

    if len(data) == 0:
        return []

    head = List.fromvalues(data).head

    p = head.next

    while p and p.val != val:
        p = p.next

    return list(List.fromhead(_delete_node(head, p)))


def _delete_node(head, node):
    """
    假设任意情况下，链表都有一个空的头指针；此外，node 一定在当前链表中。

    1. 当 node 位于链表尾部时，此时，必须要从头开始查找，故复杂度为 O(n)
    2. 当 node 位于前 n-1 位置时，此时将 node 的值用下一个节点的值覆盖，
       同时删除下一个节点即可，时间复杂度为 O(1)
    """
    if head is None:
        return

    if node is None:
        return

    if head is node:
        # node 不能指向空头节点
        return

    # 情况 1：node 位于链表尾部
    if node.next is None:
        ahead = head
        while ahead.next and ahead.next.val != node.val:
            ahead = ahead.next

        ahead.next = None
        del node
    # 情况 2：覆盖删除
    else:
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next

        # 删除下一个节点
        next_node.next = None
        del next_node

    return head


if __name__ == '__main__':
    print(delete([1, 2, 3], 3))
