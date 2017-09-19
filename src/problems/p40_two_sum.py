"""
    p40_two_sum
    ~~~~~~~~~~~~~~

    题目：和为 s 的数字

    输入一个递增排序的数组和一个数字 s，在数组中查找两个数，使得它们的和
    正好是 s。如果有多对，则输出任意一对即可。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def two_simple_stupid_way(s, seq=None):
    # 时间复杂度：O(n)
    # 空间复杂度：O(1)
    if not seq:
        return None

    left, right = 0, len(seq) - 1

    while left < right:
        tmp = seq[left] + seq[right]
        if tmp == s:
            return seq[left], seq[right]
        elif s > tmp:
            left += 1
        else:
            right -= 1

    return None


if __name__ == '__main__':
    print(two_simple_stupid_way(7, [1, 2, 3, 4, 5]))
