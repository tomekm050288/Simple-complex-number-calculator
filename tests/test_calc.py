import pytest

from calculator.calc import ComplexNumber


@pytest.mark.parametrize("input1,input2,input3,input4,expected",
                         ((3, 4, 6, 7, (9 + 11j)),
                          (3, 5, 6, 10, (9 + 15j)),
                          (1, 1, 2, 2, (3 + 3j)),
                          (9, 5, 10, 10, (19 + 15j)),
                          )
                         )
def test_add(input1, input2, input3, input4, expected):
    assert ComplexNumber(input1, input2) + ComplexNumber(input3, input4) == expected


@pytest.mark.parametrize("input1,input2,input3,input4,expected",
                         ((3, 4, 6, 7, (-3 - 3j)),
                          (3, 5, 6, 10, (-3 - 5j)),
                          (1, 1, 2, 2, (-1 - 1j)),
                          (9, 5, 10, 10, (-1 - 5j)),
                          )
                         )
def test_div(input1, input2, input3, input4, expected):
    assert ComplexNumber(input1, input2) - ComplexNumber(input3, input4) == expected


@pytest.mark.parametrize("input1,input2,input3,input4,expected",
                         ((3, 5, 6, 10, (-32+60j)),
                          (1, 5, 6, 10, (-44+40j)),
                          (1, 4, 6, 8, (-26+32j)),
                          (1, 4, 1, 8, (-31+12j)),
                          )
                         )
def test_mul(input1, input2, input3, input4, expected):
    assert ComplexNumber(input1, input2) * ComplexNumber(input3, input4) == expected

@pytest.mark.parametrize("input1,input2,input3,input4,expected",
                         ((1, 1, 2, 2, (0.5+0j)),
                          (1, 5, 5, 4, (0.6097560975609757+0.5121951219512195j)),
                          (3, 4, 2, 2, (1.75+0.25j)),
                          (1, 4, 1, 8, (0.5076923076923077-0.06153846153846154j)),
                          )
                         )
def test_div(input1, input2, input3, input4, expected):
    assert ComplexNumber(input1, input2) / ComplexNumber(input3, input4) == expected