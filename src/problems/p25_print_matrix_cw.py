"""
    p25_print_matrix_cw
    ~~~~~~~~~~~~~~

    问题：顺时针打印矩阵

    输入一个矩阵，按照从外到里，顺时针方式打印出每个元素。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

GO_RIGHT = 0
GO_DOWN = 1
GO_LEFT = 2
GO_UP = 3


def visit_matrix_in_clockwise_order(matrix, rows, columns):
    """
    定义四种状态：
    1. GO_RIGHT(initial)
    2. GO_DOWN
    3. GO_LEFT
    4. GO_UP

    四种状态是轮询切换的，触发条件分别为：
    1. GO_RIGHT->GO_DOWN: reach max_col, min_row++
    2. GO_DOWN->GO_LEFT: reach max_row, max_col--
    3. GO_LEFT->GO_UP: reach min_col, max_row--
    4. GO_UP->GO_RIGHT: reach min_row, min_col++
    """
    if not matrix:
        return None

    if rows <= 0 or columns <= 0:
        return None

    if columns == 1 or rows == 1:
        for x in matrix:
            yield from x
    else:
        max_steps = rows * columns
        status = GO_RIGHT
        min_row, min_col, max_row, max_col = 0, 0, rows - 1, columns - 1

        steps = 0
        row, col = 0, 0

        def go_right():
            nonlocal col, min_row, status
            col += 1
            if col == max_col:
                status = GO_DOWN
                min_row += 1

        def go_down():
            nonlocal row, max_col, status
            row += 1
            if row == max_row:
                status = GO_LEFT
                max_col -= 1

        def go_left():
            nonlocal col, max_row, status
            col -= 1
            if col == min_col:
                status = GO_UP
                max_row -= 1

        def go_up():
            nonlocal row, min_col, status
            row -= 1
            if row == min_row:
                status = GO_RIGHT
                min_col -= 1

        handlers = {
            GO_RIGHT: go_right,
            GO_DOWN: go_down,
            GO_LEFT: go_left,
            GO_UP: go_up
        }

        while steps < max_steps:
            steps += 1
            yield matrix[row][col]
            handlers[status]()


if __name__ == '__main__':
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(list(visit_matrix_in_clockwise_order(m, 3, 3)))
