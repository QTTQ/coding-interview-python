"""
    test_p13
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p13_matrix_has_path import matrix_has_path


def test_function_of_matrix_has_path():
    mat = [
        list('abtg'),
        list('cfcs'),
        list('jdeh')
    ]

    assert matrix_has_path(mat, 3, 3, 'a') is True
    assert matrix_has_path(mat, 3, 3, 'abt') is True
    assert matrix_has_path(mat, 3, 3, 'abfd') is True
    assert matrix_has_path(mat, 3, 3, 'abfce') is True
    assert matrix_has_path(mat, 3, 3, 'abfb') is False


def test_matrix_path_with_boundary_input():
    mat = [
        list('abtg')
    ]
    assert matrix_has_path(mat, 1, 3, 'ab') is True

    mat = [
        ['a'], ['b'], ['c']
    ]
    assert matrix_has_path(mat, 3, 1, 'ab') is True

    mat = [
        ['a', 'a', 'a'],
        ['a', 'a', 'a'],
        ['a', 'a', 'a'],
    ]
    assert matrix_has_path(mat, 3, 3, 'aaa') is True


def test_matrix_path_with_dangerous_input():
    assert matrix_has_path(None, 0, 0, 'abc') is False
    assert matrix_has_path([['a', 'b'], ['c', 'd']], 0, 2, 'abc') is False
    assert matrix_has_path([['a', 'b'], ['c', 'd']], 2, 0, 'abc') is False
    assert matrix_has_path([['a', 'b'], ['c', 'd']], 2, 2, '') is False
    assert matrix_has_path([['a', 'b'], ['c', 'd']], 2, 2, None) is False


if __name__ == '__main__':
    test_function_of_matrix_has_path()
