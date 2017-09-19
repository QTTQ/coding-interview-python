"""
    test_p39
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p39_find_num_matches_index import find_num_matches_its_index


def test_find_num_matches_its_index():
    assert find_num_matches_its_index([1, 2, 3]) is None
    assert find_num_matches_its_index([0, 2, 3]) == 0
    assert find_num_matches_its_index([-1, 1, 3]) == 1
    assert find_num_matches_its_index([-1, 0, 2]) == 2
    assert find_num_matches_its_index([1]) is None
    assert find_num_matches_its_index([0]) == 0
    assert find_num_matches_its_index([]) is None
    assert find_num_matches_its_index(None) is None
