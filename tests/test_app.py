from src.square.app import Square
import pytest

@pytest.mark.parametrize("test_input, expected", [
    (2, 4),
    (5, 25),
    (6, 36),
    (3, 9),
    (3, 900)
])

def test_multi_squares(test_input, expected):
    sq = Square(test_input)
    assert sq.area() == expected

@pytest.mark.skip(reason=" value not supported")
def test_negative_perimeter():
    sq = Square(-1)
    assert sq.perimeter() == -4


#def test_invalid_input():
    #with pytest.raises(ValueError):
    #    sq = Square(-3)