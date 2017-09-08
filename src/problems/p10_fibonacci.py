"""
    p10_fibonacci
    ~~~~~~~~~~~~~~

    题目：求斐波那契数列的第 n 项

    编写一个函数，输入 n，求 Fibonacci 数列的第 n 项
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.helpers import simple_cache


def fibonacci1(n):
    """根据定义，可以直接写出递归的实现
    但是该实现存在的问题是效率非常低，并且随着 n 的增加，时间复杂度
    是以指数形式增长
    同时在递归计算中，会重复计算很多数，严重浪费计算资源
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    return fibonacci1(n - 1) + fibonacci1(n - 2)


@simple_cache
def fibonacci2(n):
    """为了减少计算次数，我们增加一个缓存来加速计算
    这样也带来了额外的空间占用，好在可以有效提高计算
    速度
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1

    result = fibonacci1(n - 1) + fibonacci1(n - 2)
    return result


def fibonacci3(n):
    """
    从小到大的顺序进行计算，将复杂度缩减到 O(n)
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = a + b, a

    return a
