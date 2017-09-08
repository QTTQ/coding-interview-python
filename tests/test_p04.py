"""
    test_p04
    ~~~~~~~~~~~~~~

    Description of this module.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p04_find_in_sorted_matrix import (find_in_sorted_matrix,
                                                    find_in_sorted_matrix2,
                                                    find_in_sorted_matrix3)


@pytest.fixture(params=[find_in_sorted_matrix,
                        find_in_sorted_matrix2,
                        find_in_sorted_matrix3])
def func(request):
    return request.param


def test_with_invalid_matrix(func):
    assert func(None, 0, 0, -1) is False
    assert func([], 0, 0, -1) is False


@pytest.mark.parametrize('target',
                         [
                             1,
                             15,
                             8,
                             10,
                             6,
                             2
                         ])
def test_with_matrix_contains_target(func, target):
    matrix = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]
    assert func(matrix, 4, 4, target) is True


@pytest.mark.parametrize('target',
                         [0, 16, 3, 5])
def test_with_matrix_does_not_contain_target(func, target):
    matrix = [
        [1, 2, 8, 9],
        [2, 4, 9, 12],
        [4, 7, 10, 13],
        [6, 8, 11, 15]
    ]
    assert func(matrix, 4, 4, target) is False
