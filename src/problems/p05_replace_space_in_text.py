"""
    p05_replace_space_in_text
    ~~~~~~~~~~~~~~

    题目：实现一个函数，把字符串中的每个空格替换成 "%20"，如
    "We are happy" -> "We%20are%20happy"
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def replace_space_in_text(text, length):
    """
    这里的思路是要从后往前找，把字符依次往后移动，减少重复移动的次数。
    整体时间复杂度可以到 O(n)

    这里大致分为两步：
    1. 通过空格数计算字符串整体要增加的长度
    2. 从后往前扫描，并将字符串往后面移动
    """
    if not text or not isinstance(text, str):
        return ValueError('text is empty')

    # 第一次扫描，得到后移元素最后的长度（实际字符串会增加的长度）
    space_nums = 0
    text_length_original = 0

    for c in text:
        text_length_original += 1
        if c.isspace():
            space_nums += 1

    text_length_new = text_length_original + space_nums * 2
    if text_length_new > length:
        raise ValueError('buffer is not big enough')

    # 设定两个游标
    behind = text_length_new - 1
    ahead = text_length_original - 1

    # 字符串打散，同时假设存储字符串的列表中长度足够大
    # 使用列表模拟 C 中的字符串，从而能够使用 inplace 替换或移动
    text = list(text) + ['' for _ in range(length)]

    while 0 <= ahead < behind:
        c = text[ahead]
        if c.isalpha():
            # 如果是字符，则直接往后移动
            text[behind] = c
            behind -= 1
        elif c.isspace():
            # 如果是空格，则插入 "%20"
            text[behind] = '0'
            text[behind - 1] = '2'
            text[behind - 2] = '%'
            behind -= 3

        ahead -= 1

    return "".join(text)


if __name__ == '__main__':
    print(replace_space_in_text('a b c', 40))
