"""
    test_p32
    ~~~~~~~~~~~~~~
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

from src.problems.p32_num_of_one import count_total_ones_stupid_way


def test_count_total_ones():
    assert count_total_ones_stupid_way(5) == 1
    assert count_total_ones_stupid_way(10) == 2
    assert count_total_ones_stupid_way(55) == 16
    assert count_total_ones_stupid_way(99) == 20

    assert count_total_ones_stupid_way(0) == 0
    assert count_total_ones_stupid_way(1) == 1

    assert count_total_ones_stupid_way(10000) == 4001
    assert count_total_ones_stupid_way(21235) == 18690
