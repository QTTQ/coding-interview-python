"""
    test_p37
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p37_count_num_in_sorted_array import count_k_in_seq


def test_count_k_in_seq():
    assert count_k_in_seq(2, [1, 2, 2, 3, 4]) == 2
    assert count_k_in_seq(9, [1, 2, 2, 3, 4]) == 0
    assert count_k_in_seq(4, [1, 2, 2, 3, 4]) == 1
    assert count_k_in_seq(4, [4]) == 1
    assert count_k_in_seq(4, [1, 2, 3, 4, 4]) == 2
    assert count_k_in_seq(1, [1, 1, 2, 3]) == 2
    assert count_k_in_seq(1, None) == 0
