"""
    p21_adjust_odd_even_nums_in_array
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：调整数组顺序使奇数位于偶数前面

    输入一个整数数组，实现一个函数来调整该数组中的数字的顺序，
    使所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def adjust_odd_even_nums_order(values):
    """
    以下保证元素移动次数尽可能少，采用双游标法实现
    """
    if values is None:
        return None

    if len(values) <= 1:
        return values

    # 此时，数组至少有两个元素
    head, tail = 0, len(values) - 1

    while head < tail:
        # 前偶后奇
        if is_even(values[head]) and is_odd(values[tail]):
            # 交换元素
            values[head], values[tail] = values[tail], values[head]
            head += 1
            tail -= 1
        # 前奇后偶
        elif is_odd(values[head]) and is_even(values[tail]):
            head += 1
            tail -= 1

        # 前奇后奇
        elif is_odd(values[head]) and is_odd(values[tail]):
            # 期待后面有一个偶数
            head += 1

        # 前偶后偶
        elif is_even(values[head]) and is_even(values[tail]):
            # 期待前面有一个奇数
            tail -= 1

    return values


def adjust_odd_even_nums_order1(values):
    """
    以下保证元素移动次数尽可能少，采用双游标法实现
    """
    if values is None:
        return None

    if len(values) <= 1:
        return values

    # 此时，数组至少有两个元素
    head, tail = 0, len(values) - 1

    while head < tail:
        # 直到遇到一个偶数
        while head < tail and not is_even(values[head]):
            head += 1

        # 直到遇到一个奇数
        while head < tail and is_even(values[tail]):
            tail -= 1

        # 进行交换
        if head < tail:
            values[head], values[tail] = values[tail], values[head]

    return values


def reorder(values, func):
    """更加可扩展的方法"""
    if values is None:
        return None

    if len(values) <= 1:
        return values

    # 此时，数组至少有两个元素
    head, tail = 0, len(values) - 1

    while head < tail:
        # 直到遇到一个偶数
        while head < tail and not func(values[head]):
            head += 1

        # 直到遇到一个奇数
        while head < tail and func(values[tail]):
            tail -= 1

        # 进行交换
        if head < tail:
            values[head], values[tail] = values[tail], values[head]

    return values


def is_even(n):
    # 判断是不是偶数
    return n & 0x1 == 0


def is_odd(n):
    return not is_even(n)


if __name__ == '__main__':
    print(adjust_odd_even_nums_order([1, 2, 3, 4, 5]))
    print(adjust_odd_even_nums_order([1, 3, 5, 7]))
    print(adjust_odd_even_nums_order([2, 4, 6, 8]))
