"""
    test_find_duplicate_numbers
    ~~~~~~~~~~~~~~

    Description of this module.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p02_find_duplicate_numbers import find_dup_numbers1, find_dup_numbers2


@pytest.fixture(params=[find_dup_numbers1, find_dup_numbers2])
def find_dup_func(request):
    return request.param


@pytest.mark.parametrize('seq, expected',
                         [
                             (None, None),
                             ([], None),
                             ([1], None),
                             ([1, 2], None),
                             ([1, 2, 2, 3], [2]),
                             ([1, 2, 2, 3, 3], [2, 3]),
                             ([1, 2, 0, 2, 3, 3, 0], [0, 2, 3]),
                         ])
def test_find_dup_numbers(find_dup_func, seq, expected):
    if expected is None:
        assert find_dup_func(seq) is None
    else:
        assert set(find_dup_func(seq)) == set(expected)
