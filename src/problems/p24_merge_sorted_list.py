"""
    p24_merge_sorted_list
    ~~~~~~~~~~~~~~

    问题：合并两个排序链表

    输入两个递增排序的链表，合并这两个链表并使得新链表的节点仍然是排序的。

    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.datastructures.linkedlist.single import List, Node
from src.helpers import to_pylist


@to_pylist
def merge_two_sorted_list(values_left, values_right):
    """这个是一个典型的递归过程
    原则是谁小谁做最终链表的头，这样整个递归完成后，就得到有序的
    链表了。
    """
    left_head = List.fromvalues(values_left).head
    right_head = List.fromvalues(values_right).head

    # 考虑特殊情况
    if left_head is None:
        return right_head
    elif right_head is None:
        return left_head

    if left_head is None and right_head is None:
        return None

    # 指向真正的头节点
    merged_head = Node(None, None)

    def merge(left, right):
        if left is None:
            return right
        elif right is None:
            return left

        # 谁小谁做头
        if left.val > right.val:
            head = right
            head.next = merge(left, right.next)
        else:
            head = left
            head.next = merge(left.next, right)

        return head

    merged_head.next = merge(left_head.next, right_head.next)
    return merged_head


if __name__ == '__main__':
    print(merge_two_sorted_list([1, 2, 3], [4, 5]))
