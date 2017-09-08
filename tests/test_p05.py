"""
    test_p05
    ~~~~~~~~~~~~~~

    Description of this module.
    
    :copyright: (c) 2017 by 0xE8551CCB.
    :license: MIT, see LICENSE for more details.
"""

import pytest
from src.problems.p05_replace_space_in_text import replace_space_in_text


def test_replace_space_in_text():
    # 边界条件测试
    with pytest.raises(ValueError):
        _ = replace_space_in_text('', 0)
        _ = replace_space_in_text(None, 0)
        _ = replace_space_in_text('He is a monster', 10)

    assert replace_space_in_text(' ', 5) == '%20'
    assert replace_space_in_text('  ', 6) == '%20%20'
    assert replace_space_in_text(' He', 6) == '%20He'
    assert replace_space_in_text('Hello ', 12) == 'Hello%20'
    assert replace_space_in_text('Hello world', 20) == 'Hello%20world'
    assert replace_space_in_text(' Hello ', 20) == '%20Hello%20'
