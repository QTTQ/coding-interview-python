"""
    01_find_kth_node
    ~~~~~~~~~~~~~~

    题目描述：求链表中倒数第 k 个节点。

    当我们用一个指针遍历链表不能解决问题时，就可以尝试使用两个指针。
    可以让其中一个指针遍历的快一点（如一次走两步），或者让它先在
    链表上走若干步，直到走到结尾。
    比如，求一个链表的中间节点，就可以使用两个指针，前指针一次走两步，
    后指针一次走一步，当前指针走到头之后，后指针就所在的位置就是中间
    节点。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def find_kth_node(head, k):
    """思路是设置两个指针，分别为 ahead, behind，前指针先走
    k-1 步，然后 ahead 和 behind 同步向后走，直到 ahead
    走到最后，此时 behind 所在的位置就是倒数第 k 个节点了。

    考虑边界条件：
    1. 空链表
    2. k 为 0
    3. total_length < k
    """
    if head is None:
        return None

    if k < 1:
        return None

    behind, ahead = head.next, head.next

    for _ in range(k - 1):
        # 头指针先走 k -1 步
        ahead = ahead.next

        if ahead is None:
            # 防止走过头了，可能链表长度不够
            return None

    # 前后指针共同往后走
    while ahead.next:
        ahead = ahead.next
        behind = behind.next

    # behind 所指向的就是相应的节点
    return behind


if __name__ == '__main__':
    from src.datastructures.linkedlist.single import List

    l = List.fromvalues([1])
    print(find_kth_node(l.head, 1))
