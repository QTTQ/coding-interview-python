"""
    p22_find_entry_of_partial_circular_list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：链表中环的入口节点

    如果一个链表中包含环，则如何找出环中的入口节点？
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.datastructures.linkedlist.single import List


def build_partial_circular_list(values, entry_value):
    """构建部分环形的链表"""
    if values is None:
        return None

    values = List.fromvalues(values)

    # 查找 entry 节点
    entry_node = values.find_node(entry_value)
    last_node = values.find_node(values[-1])
    last_node.next = entry_node
    return values.head


def find_entry_node_in_partial_circular_list(values, entry_value):
    """设置两个指针，一个在前面，一个再后面，让前面的走得比后面的快一点
    这样当二者相遇时，就能判断是否存在环，以及出现环的节点了。"""
    if len(values) == 0:
        return None

    head = build_partial_circular_list(values, entry_value)

    if head.next is None:
        return None

    ahead, behind = head.next.next, head.next

    while ahead.next and ahead != behind:
        ahead = ahead.next.next
        behind = behind.next

    if ahead.next:
        return ahead.next.val

    return None


if __name__ == '__main__':
    print(find_entry_node_in_partial_circular_list([1, 2, 3, 4], 2))
