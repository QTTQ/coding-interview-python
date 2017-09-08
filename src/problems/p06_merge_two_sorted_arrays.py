"""
    p06_merge_two_sorted_array
    ~~~~~~~~~~~~~~

    有两个分别排序（升序）的数组 A 和 B，并且 A 数组有足够大的空间可以容纳 B
    要求设计一个函数，实现将 B 中的元素插入到 A 并且保证最后数组也是有序的。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def merge_two_sorted_arrays(seq_a, length_a, seq_b, length_b):
    """这道题是 p05 的同类题目，我们同样以从后往前查找并按需移动来完成
    需求，同时保证时间复杂度较低（O(m+n))

    这里我们假设 seq_a 是一个长度为（length_a + length_b）的数组空间
    """
    if seq_a and not seq_b:
        return seq_a

    if not seq_a and seq_b:
        return seq_b

    if not (seq_a and seq_b):
        return None

    # 考虑两个游标分别指向 seq_a 和 seq_b 的尾部，并且同时移动游标
    # 在移动过程中比较元素大小，将较大的元素后置
    cursor_a, cursor_b = length_a - 1, length_b - 1
    tail = length_a + length_b - 1

    # 注意临界条件的选择
    while cursor_b >= 0 and tail >= 0:
        # 不断移动较大的数到最后去
        while cursor_a >= 0 and seq_a[cursor_a] > seq_b[cursor_b]:
            seq_a[tail] = seq_a[cursor_a]
            tail -= 1
            cursor_a -= 1
        else:
            seq_a[tail] = seq_b[cursor_b]
            tail -= 1

        cursor_b -= 1

    return seq_a


if __name__ == '__main__':
    print(merge_two_sorted_arrays([3, 4, None, None, None], 2, [0, 1, 2], 3))
