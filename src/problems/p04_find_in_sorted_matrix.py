"""
    p04_find_in_sorted_matrix
    ~~~~~~~~~~~~~~

    题目：二维数组查找

    在一个二维数组中，每一行都是按照从左到右的递增顺序排列的，每一列则按照从上到下
    递增顺序排列。要求完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否
    含有该整数。
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""


def find_in_sorted_matrix(matrix, rows, colums, target):
    """借助二分查找，可以在 O(nlogn) 的时间复杂度内完成查找"""
    if matrix is None:
        return False

    for row in matrix:
        if binary_search(row, target):
            return True
    else:
        return False


def binary_search(seq, target):
    if seq is None:
        return False

    low, high = 0, len(seq) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if seq[mid] > target:
            high = mid - 1
        elif seq[mid] < target:
            low = mid + 1
        else:
            return True
    else:
        return False


def find_in_sorted_matrix2(matrix, rows, columns, target):
    """选取右上角，然后每次比较都可以剔除一列或者一行，从而加快速度完成查找
    具体而言，假设选择的数字为 k，则有三种情况：
    1. k == target：此时直接返回即可
    2. k < target：剔除 k 所在的行（行号递增即可）
    3. k > target：剔除 k 所在的列（列号递减即可）
    """

    if matrix is None or rows <= 0 or columns <= 0:
        return False

    row, col = 0, columns - 1
    while row < rows and col >= 0:
        k = matrix[row][col]
        if k == target:
            return True
        elif k < target:
            row += 1
        elif k > target:
            col -= 1
    else:
        return False


def find_in_sorted_matrix3(matrix, rows, columns, target):
    """和上面的算法类似，但是使用左下角作为参考"""
    if matrix is None or rows <= 0 or columns <= 0:
        return False

    row, col = rows - 1, 0
    while row >= 0 and col < columns:
        k = matrix[row][col]
        if k == target:
            return True
        elif k < target:
            col += 1
        else:
            row -= 1
    else:
        return False


if __name__ == '__main__':
    matrix_ = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]
    print(find_in_sorted_matrix(matrix_, 10))
    print(find_in_sorted_matrix2(matrix_, 4, 4, 10))
    print(find_in_sorted_matrix3(matrix_, 4, 4, 10))
    print(find_in_sorted_matrix(matrix_, 4))
    print(find_in_sorted_matrix2(matrix_, 4, 4, 4))
    print(find_in_sorted_matrix3(matrix_, 4, 4, 4))
    print(find_in_sorted_matrix(matrix_, 5))
    print(find_in_sorted_matrix2(matrix_, 4, 4, 5))
    print(find_in_sorted_matrix3(matrix_, 4, 4, 5))
