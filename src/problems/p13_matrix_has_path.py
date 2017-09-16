"""
    p13_matrix_has_path
    ~~~~~~~~~~~~~~~~~~~

    问题：设计一个函数，判断矩阵中是否存在一条包含某个字符串所有
    字符的路径。路径可以从矩阵中的任意一个位置开始，每一步可以
    在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵中的
    某一格，那么该路径就不能再次进入该格子。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def matrix_has_path(matrix, rows, columns, target):
    """这道题的重点是使用回溯的方法来进行匹配，在这里由于可能需要回到上一步，
    所以可以使用栈来存储之前的节点（用递归实现），其次需要记录哪些路径已经
    访问过了，所以还需要一个额外的矩阵空间来记录当前已经访问过的路径。
    """
    if matrix is None or rows < 1 or columns < 1 \
            or not target:
        return False

    # 记录节点是否访问过
    visited = [[False for _ in range(columns)] for _ in range(rows)]
    path_len = 0

    def _check_has_path(row, col):
        nonlocal path_len

        if path_len == len(target):
            return True

        _has_path = False
        if 0 <= row < rows and 0 <= col < columns \
                and matrix[row][col] == target[path_len] \
                and not visited[row][col]:
            # 检查下一个字符
            path_len += 1

            visited[row][col] = True
            _has_path = _check_has_path(row, col - 1) or \
                        _check_has_path(row - 1, col) or \
                        _check_has_path(row, col + 1) or \
                        _check_has_path(row + 1, col)

            if not _has_path:
                # 进行一次回溯
                path_len -= 1
                visited[row][col] = False

        return _has_path

    for row_ in range(rows):
        for col_ in range(columns):
            has_path = _check_has_path(row_, col_)
            if has_path:
                return True

    return False
