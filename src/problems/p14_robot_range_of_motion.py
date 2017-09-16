"""
    p14_robot_range_of_motion
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    题目：机器人的活动范围

    地上有一个 m 行 n 列的方格。一个机器人从坐标 (0, 0) 的格子开始移动，
    它每次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标数位和大于
    k 的格子。例如，当 k = 18 时，机器人能够进入方格 (35, 37)，此时 3+5+3+7 = 18，
    而不能进入 (35, 38)。问，机器人能够到达的格子有多少个？
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def moving_count(rows, columns, threshold):
    """同样，这个是利用回溯的方法进行计算。假设机器人可以进入
    坐标 (i, j) 的格子，则判断它能否进入 4 个相邻的格子
    (i, j-1), (i, j+1), (i-1, j), (i+1, j)。"""
    if rows <= 0 or columns <= 0 or threshold < 0:
        return 0

    visited = [[False for _ in range(columns)] for _ in range(rows)]

    def sum_digits(num):
        s = 0
        while num > 0:
            s = s + (num % 10)
            num //= 10
        return s

    def count(row, col):
        cnt = 0

        ok = (0 <= row < rows
              and 0 <= col < columns
              and not visited[row][col]
              and sum_digits(row) + sum_digits(col) <= threshold)
        if ok:
            # print(row, col)
            visited[row][col] = True
            cnt = (1 +
                   count(row, col - 1) +
                   count(row - 1, col) +
                   count(row, col + 1) +
                   count(row + 1, col))
        return cnt

    return count(0, 0)
