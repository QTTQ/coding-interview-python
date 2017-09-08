"""
    test_p03
    ~~~~~~~~~~~~~~

    Description of this module.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p03_find_duplicate_numbers2 import find_dup_numbers


@pytest.mark.parametrize('seq, expected',
                         [
                             (None, None),
                             ([], None),  # n = 0
                             ([1, 1], [1]),  # n = 1
                             ([1, 2, 2], [2]),  # n = 2
                             ([2, 2, 3, 2], [2, 3]),  # n = 3
                         ])
def test_find_dup_numbers(seq, expected):
    if expected is None:
        assert find_dup_numbers(seq) is None
    else:
        assert find_dup_numbers(seq) in expected
