"""
    p22_find_entry_of_partial_circular_list
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：链表中环的入口节点

    如果一个链表中包含环，则如何找出环中的入口节点？
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.datastructures.linkedlist.single import List


def find_entry_in_partial_circle_list(values, entry_value):
    # 第一步：构建带环的链表
    head = build_partial_circular_list(values, entry_value)

    # 第二步：判断是否有环存在
    node = find_circle(head)

    # 第三步：计算环中包含多少个节点
    num_of_nodes = count_nodes_in_circle(node)

    # 第四步：查找入口节点
    return find_entry(head, num_of_nodes)


def build_partial_circular_list(values, entry_value):
    """构建部分环形的链表"""
    if values is None:
        return None

    values = List.fromvalues(values)

    if entry_value is not None:
        # 查找 entry 节点
        entry_node = values.find_node(entry_value)
        last_node = values.find_node(values[-1])
        last_node.next = entry_node

    return values.head


def find_circle(head):
    """
    该函数负责判断链表是否存在环，如果存在则返回环中的节点，
    否则返回 None

    思路是设置两个指针，快的比慢的要多走一步，等到二者相遇时，
    则表明链表中存在环
    """
    if head is None:
        return None

    slow = head.next
    if slow is None:
        return None

    fast = slow.next

    while fast and slow:
        if fast == slow:
            return fast

        slow = slow.next
        fast = fast.next
        if fast:
            fast = fast.next

    return None


def count_nodes_in_circle(node):
    """计算环中有多少个节点"""
    if node is None:
        return 0

    cnt = 1
    p = node
    while p.next != node:
        cnt += 1
        p = p.next

    return cnt


def find_entry(head, nodes_in_circle):
    """
    思路：设置两个指针，前指针先走 nodes_in_circle 步，
    然后，后指针和前指针一块移动，当后指针追到前指针时，所
    指向的位置就是入口节点了。
    """
    if head is None:
        return None

    if nodes_in_circle <= 0:
        return None

    behind, ahead = head.next, head.next

    # 前指针先走几步
    while nodes_in_circle > 0:
        ahead = ahead.next
        nodes_in_circle -= 1

    while ahead != behind:
        ahead = ahead.next
        behind = behind.next

    return behind.val
