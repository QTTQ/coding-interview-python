"""
    p27_push_pop_sequence_in_stack
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    问题：栈的压入、弹出序列

    输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
    假设压入栈的所有数字均不相等。例如，序列 [1, 2, 3, 4, 5] 为某栈的压入序列，序列
    [4, 5, 3, 2, 1] 是该压入序列对应的一个弹出序列，但 [4, 3, 5, 1, 2] 就不是。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.datastructures.stack import Stack


def is_possible_out_sequence(in_stack_seq, out_stack_seq):
    """思路：
    1. 设定两个游标，分别指向 in 和 out 序列
    2. 遍历 in 序列，依次入栈，在栈顶元素等于 out 序列当前元素时，
    弹出栈顶元素，并将 out 游标移动到下一个位置
    3. 重复直到 in 序列完全扫描完后，开始出栈，每次出栈，都对比 out 指向元素，
    如果相等则移动，不等则失败。
    """
    if in_stack_seq is None:
        return False

    if out_stack_seq is None:
        return False

    if len(in_stack_seq) == 0 or len(out_stack_seq) == 0:
        return False

    if len(in_stack_seq) != len(out_stack_seq):
        return False

    stack = Stack()
    out_cursor = 0

    for x in in_stack_seq:
        if x != out_stack_seq[out_cursor]:
            stack.push(x)
        else:
            out_cursor += 1
            # 如果此时栈顶元素等于当前指向 out 序列的元素，就出出栈，直到栈为空
            while not stack.is_empty() and \
                            stack.peek() == out_stack_seq[out_cursor]:
                stack.pop()
                out_cursor += 1

    return stack.is_empty()


if __name__ == '__main__':
    # print(is_possible_out_sequence([1, 2, 3], [3, 2, 1]))
    # print(is_possible_out_sequence([1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))
    print(is_possible_out_sequence([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))
