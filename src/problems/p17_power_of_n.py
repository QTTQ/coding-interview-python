"""
    p17_power_of_n
    ~~~~~~~~~~~~~~

    题目：数值的整数次方

    实现函数 power(base, exponent)，求 base 的 exponent 次方。
    不考虑大数的情况（这对类似 C 语言的情况下，不用考虑整数溢出问题）

    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def power1(base, exponent):
    if base == 0:
        return 0

    if exponent == 0:
        return 1

    if exponent == 1:
        return base

    # 考虑负数的情况
    is_positive = True

    if exponent < 0:
        is_positive = False
        exponent = -exponent

    result = 1
    while exponent:
        result *= base
        exponent -= 1

    # 当 result 为 0 时，会自动抛出异常
    return result if is_positive else 1 / result


def power2(base, exponent):
    """
    利用公式求解：

    n 为偶数时
    a^n = a^(n/2) * a^(n/2)

    n 为奇数时
    a^n = a^((n-1)/2) * a^((n-1)/2) * a
    """
    if base == 0:
        return 0

    if exponent == 0:
        return 1

    if exponent == 1:
        return base

    # 考虑负数的情况
    is_positive = True

    if exponent < 0:
        is_positive = False
        exponent = -exponent

    result = _get_result(base, exponent)
    return result if is_positive else 1 / result


def _get_result(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base

    # 使用位移，优化运算速度
    result = _get_result(base, exponent >> 1)
    result *= result

    # 判断是否是奇数
    if exponent & 0x01 == 1:
        result *= base

    return result
