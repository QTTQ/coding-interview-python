"""
    p12_find_smallest_in_rotated_array
    ~~~~~~~~~~~~~~
    题目：旋转数组的最小数字

    把一个数组最开始的若干个元素搬到数组的末尾，称为数组的旋转。输入一个递增排序的数组的一个旋转，
    输出旋转数组的最小值

    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def find_smallest_number1(rotated_array):
    """最简单的算法自然是做一次扫描，但是复杂度为 O(n)，
    此外，没有用到旋转数组的特性。
    """
    if rotated_array is None or len(rotated_array) == 0:
        return None

    min_value = rotated_array[0]
    for i in range(1, len(rotated_array)):
        if rotated_array[i] < min_value:
            min_value = rotated_array[i]

    return min_value


def find_smallest_number2(rotated_array):
    """考虑采用二分的方式进行查找：O(logn)
    旋转数组的左右两个部分一定是排序的，所以可以设置两个游标（begin, end），分别指向首尾，
    那么根据定义，一般情况下 begin 的元素一定是大于等于 end 的元素（除非旋转了 0 次，即
    最初的有序数组），那么 mid 的元素要么落在左侧递增区间，要么落在右侧递增区间，通过不断
    循环，到 begin 和 end 的距离为 1 时停止查找，此时 mid 所指向的就是最小的元素。
    考虑特殊情况 array[begin] == array[end] == array[mid] 的时候，将无法决定 begin
    和 end 的变化，此时，需要在相应区间执行顺序查找。
    """
    if rotated_array is None or len(rotated_array) == 0:
        return None

    begin, end = 0, len(rotated_array) - 1
    # 如果旋转次数为 0，则直接返回
    mid = begin

    def find_min_inorder(from_, to):
        min_value = rotated_array[from_]

        for i in range(from_ + 1, to):
            if min_value > rotated_array[i]:
                min_value = rotated_array[i]

        return min_value

    while rotated_array[begin] >= rotated_array[end]:
        if begin + 1 == end:
            break

        mid = begin + (end - begin) // 2
        # 特殊情况：[1, 0, 1, 1, 1], [1, 1, 1, 0, 1]
        if rotated_array[begin] == rotated_array[end] \
                and rotated_array[mid] == rotated_array[begin]:
            return find_min_inorder(begin, end + 1)
        if rotated_array[mid] >= rotated_array[begin]:
            begin = mid
        elif rotated_array[mid] <= rotated_array[mid]:
            end = mid

    return rotated_array[mid]


if __name__ == '__main__':
    print(find_smallest_number2([3, 4, 5, 0, 0, 0]))
