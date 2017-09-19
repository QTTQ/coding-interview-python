"""
    p35_first_not_repeating_char
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：第一个只出现一次的字符

    1. 在字符中找出第一个只出现一次的字符，如输入 "abaccdeff"，则输出 'b'

    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""
from collections import defaultdict


def first_not_repeating_char_in_string(s):
    """
    使用字典记录字符出现的次数：
    1. 第一次扫描：计数
    2. 第二次扫描：读取次数为 1 的字符
    """
    if not s:
        return None

    seen = defaultdict(int)

    for c in s:
        seen[c] += 1

    for c in s:
        if seen[c] == 1:
            return c

    return None
