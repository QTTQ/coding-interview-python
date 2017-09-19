"""
    p34_ugly_number
    ~~~~~~~~~~~~~~

    问题：丑数

    我们把包含因子 2、3 和 5 的数字叫做丑数，求从小到大的顺序的第 1500 个丑数。
    例如：6、8 都是丑数，但 14 不是，因为它包含因子 7。习惯上我们把 1 当做第一
    个丑数。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def get_ugly_number_1(index):
    """
    计算所有的丑数，直到第 index 个为止。
    """
    if index < 1:
        return None

    num = 0
    while index > 0:
        num += 1
        if is_ugly(num):
            index -= 1

    return num


def is_ugly(n):
    """2、3 和 5 的因子"""
    while n % 2 == 0:
        n //= 2

    while n % 3 == 0:
        n //= 3

    while n % 5 == 0:
        n //= 5

    return n == 1


def get_ugly_number_2(index):
    # 用空间换时间：生成一个大小为 index 的丑数数组
    # 这个丑数数组是按从小到大的顺序排列的
    if index < 1:
        return None

    ugly_numbers = [1]
    next_index = 1

    multi_two_index = 0
    multi_three_index = 0
    multi_five_index = 0

    while next_index < index:
        min_val = min(ugly_numbers[multi_two_index] * 2,
                      ugly_numbers[multi_three_index] * 3,
                      ugly_numbers[multi_five_index] * 5)
        ugly_numbers.append(min_val)

        while (ugly_numbers[multi_two_index] * 2 <= ugly_numbers[next_index]
               and multi_two_index < next_index):
            multi_two_index += 1

        while (ugly_numbers[multi_three_index] * 3 <= ugly_numbers[next_index]
               and multi_three_index < next_index):
            multi_three_index += 1

        while (ugly_numbers[multi_five_index] * 5 <= ugly_numbers[next_index]
               and multi_five_index < next_index):
            multi_five_index += 1

        next_index += 1

    return ugly_numbers[index - 1]


if __name__ == '__main__':
    print(get_ugly_number_2(10))
