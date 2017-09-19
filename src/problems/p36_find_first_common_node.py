"""
    p36_find_first_common_node
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    问题：两个链表的第一个公共节点

    输入两个链表，找出他们的第一个公共节点。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.datastructures.linkedlist.single import List, Node


def build_two_list_with_common_nodes(seq1, seq2, common_nodes=None):
    if seq1 is None and seq2:
        return List.fromvalues(seq2).head

    if seq1 and seq2 is None:
        return List.fromvalues(seq1).head

    l1 = List.fromvalues(seq1)
    l2 = List.fromvalues(seq2)

    if common_nodes is None or len(common_nodes) < 1:
        return l1.head, l2.head

    last_node1 = l1.find_node(l1[-1])
    last_node2 = l2.find_node(l2[-1])

    l1.head.val += len(common_nodes)
    l2.head.val += len(common_nodes)

    common_node = Node(common_nodes[0], None)
    last_node1.next = common_node
    last_node2.next = common_node

    for x in common_nodes[1:]:
        common_node.next = Node(x, None)
        common_node = common_node.next

    return l1.head, l2.head


def find_first_common_node_1(head1, head2):
    """
    愚蠢的思路：

    1. 设两个游标，分别指向 head1, head；设一个集合记录二者扫描过的节点
    2. 一旦二者扫描的节点相同，则立即退出

    O(m+n) 时间复杂度和最大 O(m+n) 的空间复杂度
    """

    if head1 is None or head2 is None:
        return None

    seen = set()

    p, q = head1.next, head2.next
    while p:
        # 所有 p 扫描的节点都放到集合
        seen.add(p)
        p = p.next

    while q and q not in seen:
        q = q.next

    if q is not None:
        return q.val
    return None


def find_first_common_node_2(head1, head2):
    """
    不需要辅助空间的思路：
    1. 计算出两个链表的长度
    2. 长的链表先走一定步数，让两个链表齐头前进
    3. 当二者都指向同一节点结束
    """
    if head1 is None or head2 is None:
        return None

    length_1 = _get_length(head1)
    length_2 = _get_length(head2)

    p, q = head1.next, head2.next

    if length_1 > length_2:
        # p 走若干步
        steps = length_1 - length_2
        while p and steps > 0:
            p = p.next
            steps -= 1
    else:
        # q 走若干步
        steps = length_2 - length_1
        while q and steps > 0:
            q = q.next
            steps -= 1

    # 二者一起往后走，直到遇到相同的节点

    while p and q:
        if p is q:
            return p.val

        p = p.next
        q = q.next

    return None


def _get_length(head):
    if head is None:
        return 0
    return head.val


if __name__ == '__main__':
    h1, h2 = build_two_list_with_common_nodes([1, 2], [4, 5, 6], common_nodes=[10, 11, 12])
    print(List.fromhead(h1))
    print(List.fromhead(h2))

    print(find_first_common_node_2(h1, h2))
    print(_get_length(h1))
