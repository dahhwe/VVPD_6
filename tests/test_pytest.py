import pytest
from .. import is_cbs
from .. import need_to_move


@pytest.mark.parametrize('str_to_check, result',
                         [('((<<>>))', 1), (')<', 0)])
def test_valid_cbs(str_to_check, result):
    assert is_cbs.is_cbs(str_to_check) == result


def test_not_valid_cbs():
    assert is_cbs.is_cbs('(()(') == 0


def test_invalid_input_cbs():
    assert is_cbs.is_cbs('ABOBA') == 0


def test_number_of_moves_to_make_cbs():
    assert need_to_move.need_to_move('<()<') == 2


def test_invalid_input_need_to_move():
    assert need_to_move.need_to_move('asd12') == 5
