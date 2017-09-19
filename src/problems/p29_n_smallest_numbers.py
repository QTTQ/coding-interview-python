"""
    p29_n_smallest_numbers
    ~~~~~~~~~~~~~~~~~~~~~~

    题目：最小的 k 个数

    输入 n 个整数，找出其中最小的 k 个数。例如，输入 [4, 5, 1, 2, 7, 6, 3, 8]
    最小的 4 个数为 [1, 2, 3, 4]
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def n_smallest_numbers(n, seq=None):
    """
    最简单的方法是使用标准库 `heapq`，当 n 远小于数组的长度
    时，利用 `heapq.nsmallest` 函数即可获得。
    """
    from heapq import nsmallest

    if seq is None:
        return None

    if n > len(seq):
        return None

    return nsmallest(n, seq)


def n_smallest_numbers1(n, seq=None):
    """
    另外一种思路（特别适合海量数据的情况）：
    考虑 n 远小于数组长度（如海量数据）的情况，此时假设不能一次加载
    所有数据，那么可以维护一个大小为 n 的容器

    当容器未满时，每次将新元素加入到容器中；当容器满了后，我们需要将
    容器中最大值找出来：
    1. 如果最大值小于当前的值，则无需操作
    2. 如果最大值大于当前的值，则替换

    所以我们要做的是在该容器上实现较高效率的操作（查找最大数、插入、删除）：
    1. 使用大根堆，这样可以实现每次以 O(1) 时间获取最大值，O(log n) 时间
       插入值
    2. 使用 max，查找时间可能为 O(n)

    整体最佳复杂度可以到 O(n * log k)
    """
    if n == 0:
        return None

    if seq is None:
        return None

    if n > len(seq):
        return None

    # 该容器存放最小的 k 个数
    numbers = []

    # 同样，我们使用 heapq 模块，利用堆快速获取最大值
    from heapq import heappush, heapreplace
    for x in seq:
        if len(numbers) >= n:
            # 获取最大值
            largest_num = -numbers[0]

            # 最大的那个值肯定不会 n 个小值之一
            if x < largest_num:
                heapreplace(numbers, -x)
        else:
            # 注意，默认建立小根堆，所以取反后间接建立大根堆
            heappush(numbers, -x)

    return {-x for x in numbers}
