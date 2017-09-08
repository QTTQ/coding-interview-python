"""
    p02_find_duplicate_numbers
    ~~~~~~~~~~~~~~

    问题：找出数组中重复的数字

    在一个长度为 n 的数组里，所有数字都在 0~n-1 范围内。数组中某些数字是重复的，但不知道
    有几个数字重复了，也不知道每个数字重复了几次，要求找出任意一个重复的数字。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from collections import deque


def merge_sort(seq):
    if seq is None or len(seq) <= 1:
        return seq

    def merge(left_part, right_part):
        merged, left_part, right_part = deque(), deque(left_part), deque(right_part)
        while left_part and right_part:
            merged.append(left_part.popleft() if left_part[0] < right_part[0] else right_part.popleft())

        merged.extend(left_part if left_part else right_part)
        return list(merged)

    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


def find_dup_numbers1(seq):
    if seq is None or len(seq) <= 1:
        return None

    # 对数组排序再进行查找
    seq = merge_sort(seq)

    seen = []
    for i in range(1, len(seq)):
        if seq[i - 1] == seq[i]:
            seen.append(seq[i])

    return seen or None


def find_dup_numbers2(seq):
    if seq is None or len(seq) <= 1:
        return None

    # 使用集合记录
    seen = set()
    dup = []

    for x in seq:
        if x not in seen:
            seen.add(x)
        else:
            dup.append(x)

    return dup or None


if __name__ == '__main__':
    print(find_dup_numbers1([13, 3, 2, 1, 2, 8, 1]))
    print(find_dup_numbers2([13, 3, 2, 1, 2, 8, 1]))
