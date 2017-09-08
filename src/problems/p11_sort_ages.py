"""
    p11_sort_ages
    ~~~~~~~~~~~~~~

    题目：为公司员工的年龄进行排序

    要求实现一个排序算法，对一组年龄进行排序。要求时间复杂度为 O(n)，可以
    使用常量大小的辅助空间。待排序的数组大小假设为 5 万。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def sort_ages(seq=None, min_age=16, max_age=70):
    """年龄排序
    若只是生搬硬套一些排序算法的话，符合常量辅助空间的简单排序算法可以为：冒泡、插入、
    选择和堆排序。但由于要求时间复杂度为 O(n)，则可以发现没有任何一种算法符合要求。

    此时，我们就要换位思考，摆脱定式思维，结合题目的要求编写排序算法。考虑到年龄为整数，
    并且范围固定（假设为 0~100），那么可以预先使用一个定长数组来记录输入的年龄，并在对应
    的槽中记录个数，最后输出槽中个数不为 0 的所有元素，最终得到排序后的结果。
    """
    if seq is None or len(seq) < 1:
        return seq

    slots = [0 for _ in range(100)]  # O(100)

    for x in seq:
        if min_age <= x <= max_age:
            slots[x] += 1
        else:
            raise ValueError('age is out of range: {}'.format(x))

    tail = 0

    for age, count in enumerate(slots):
        if count == 0:
            continue

        while count > 0:
            # populate element
            seq[tail] = age
            tail += 1
            count -= 1

    return seq


if __name__ == '__main__':
    print(sort_ages([10, 12, 89, 13, 88, 10, 27, 22, 12, 54, 27]))
