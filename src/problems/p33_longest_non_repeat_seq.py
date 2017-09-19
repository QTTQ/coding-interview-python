"""
    p33_longest_non_repeat_seq
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：最长不重复子串

    请从字符串中找出一个最长的不包含重复字符的子字符串，计算该子字符串的
    长度。假设字符串中只包含 'a~z' 的字符。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def longest_unique_substr(s):
    if not s:
        return 0

    # 提示：我们可以将字典换成一个数组，数组的下表等于字符 c，这样
    # 在对应的下表（字符）槽中存放该字符上次出现的位置即可。
    seen = {}
    maxlen = 0
    behind = 0

    for ahead, c in enumerate(s):
        if c in seen and seen[c] >= behind:
            behind = seen[c] + 1
        else:
            maxlen = max(maxlen, ahead - behind + 1)
        seen[c] = ahead

    return maxlen


if __name__ == '__main__':
    print(longest_unique_substr('arabcacfr'))
