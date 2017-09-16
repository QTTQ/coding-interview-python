"""
    p20_match_regex
    ~~~~~~~~~~~~~~

    题目：正则表达式匹配

    实现一个函数用来匹配包含 '.' 和 '*' 的正则表达式。模式中的字符
    '.' 表示任意一个字符，而 '*' 表示它前面可以出现任意次（可以是 0
    次）。本题中，匹配是指字符串的所有字符匹配整个模式。

    如字符串 'aaa' 与模式 'a.a' 和 'ab*ac*a' 匹配，但与 'aa.a'
    和 'ab*a' 不匹配。

    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def match(s, pattern):
    assert isinstance(s, str)
    assert isinstance(pattern, str)

    if not s or not pattern:
        return False

    str_index, pattern_index = 0, 0
    return _match_pattern(s, str_index, pattern, pattern_index)


def _match_pattern(s, str_index, pattern, pattern_index):
    """
    考虑不同的状态下，如何移动游标。
    这里使用非确定有限状态机表示。
    """
    if len(s) == str_index + 1 \
            and len(pattern) == pattern_index + 1:
        # 全部匹配完成了
        return True

    if str_index + 1 < len(s) \
            and pattern_index + 1 == len(pattern):
        # 模式已经结束，但字符串未扫描完
        return False

    if pattern[pattern_index + 1] == '*':
        if (pattern[pattern_index] == s[str_index] or
                (pattern[pattern_index] == '.' and
                         len(s) != str_index + 1)):
            # 转换到下一个状态
            result = (_match_pattern(s, str_index + 1, pattern, pattern_index + 2)
                      or _match_pattern(s, str_index + 1, pattern, pattern_index)
                      or _match_pattern(s, str_index, pattern, pattern_index + 2))
            return result
        else:
            return _match_pattern(s, str_index, pattern, pattern_index + 2)

    if (pattern[pattern_index] == s[str_index]
        or (pattern[pattern_index] == '.'
            and str_index + 1 != len(s))):
        return _match_pattern(s, str_index + 1, pattern, pattern_index + 1)

    return False
