"""
    p30_middle_number_of_data_stream
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：数据流的中位数

    如何获得一个数据流的中位数？如果从数据流中读出奇数个值，则中位数是所有
    数值排序后位于中间的值；如果为偶数个，则中位数是所有数值排序后中间两个
    数的平均值。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from heapq import heappush, heappushpop


def get_medium(seq_iter=None):
    """
    考虑两个指针（P1, P2），都指向已经读入的数据流的中间部分，则：
    1. 当读入的个数为奇数时，P1=P2，中位数即为 P1 指向的数
    2. 当读入的个数为偶数时，P1+1=P2，中位数即为 P1 和 P2 指向数的均值

    因此将已读入的数据分成两个部分，左边部分小于右边部分。所以考虑建立两个堆：
    1. 左边为大根堆，右边为小根堆
    2. 左边所有值均小于右边
    3. 左边最大值小于右边最小值

    为了平均分配，当读入数据个数为偶数时，将数据放到小堆，否则进入大堆：
    1. 当新数据放入小堆时，判断此时该数字是否小于大堆所有数，如果大于，直接入堆；
       否则，将该数据插入到大堆，同时弹出大堆最大值放到小堆，这样维持平衡。
    2. 当新数据放入大堆时，如果该数据比小堆中的所有数都小，则直接入大堆；
       否则，将该数据插入到小堆，同时从小堆中弹出最小值，放入到大堆中，维持平衡。
    """
    if seq_iter is None:
        return None

    try:
        iter(seq_iter)
    except TypeError:
        raise TypeError('Only iterable value are accepted')

    max_heap, min_heap = [], []

    for i, x in enumerate(seq_iter, 1):
        # 偶数入小堆
        if iseven(i):
            # 该数大于大堆所有数，直接入小堆
            if len(max_heap) > 0 and x >= -max_heap[0]:
                heappush(min_heap, x)
            else:
                temp = heappushpop(max_heap, x)
                heappush(min_heap, -temp)

        # 奇数入大堆
        else:
            # 该数小于小堆所有的数
            if len(min_heap) > 0 and x < min_heap[0]:
                heappush(max_heap, -x)
            else:
                temp = heappushpop(min_heap, x)
                heappush(max_heap, -temp)

    if len(max_heap) + len(min_heap) == 0:
        return None

    if iseven(len(max_heap) + len(min_heap)):
        return (-max_heap[0] + min_heap[0]) / 2
    else:
        return -max_heap[0]


def iseven(n):
    return n & 0x1 == 0


if __name__ == '__main__':
    print(get_medium([]))
