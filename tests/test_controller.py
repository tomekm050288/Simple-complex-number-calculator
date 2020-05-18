from calculator.controller import Controller
import json
import pytest

@pytest.fixture(name="controller")
def create_controller():
    controller = Controller()
    controller.path = "result_test.json"
    return controller


def test_load_results(controller):
    controller.results = None
    assert type(controller.load_results()) is dict


def test_add_result(controller):
    controller.results = {}
    controller.add_result("result", "multiple")
    with open(controller.path) as file_json:
        result = json.load(file_json)
    assert result == {"multiple": "result"}


@pytest.mark.parametrize("input1,input2,input3,input4,operation,expected",
                         ((3, 5, 6, 10, '*', (-32+60j)),
                          (1, 5, 6, 10, '+', (7+15j)),
                          (1, 4, 6, 8, "-", (-5-4j)),
                          (1, 4, 1, 8, "/", (0.5076923076923077-0.06153846153846154j)),
                          )
                         )
def test_action(input1, input2, input3, input4, operation, expected, controller):
    assert controller.action(input1, input2, input3, input4, operation) == expected



def test_create_tuple(controller):
    complex_result = controller.action(3, 5, 6, 10, '*')
    result = controller.create_tuple(complex_result)
    assert type(result) is tuple
    assert result[0] == str((-32+60j))


def test_sort_results1(controller):
    if len(controller.results.keys()) > 1:
        sorted_results = controller.sort_results()
        assert eval(list(sorted_results.items())[0][1][0]).imag < eval(list(sorted_results.items())[1][1][0]).imag
        assert eval(list(sorted_results.items())[1][1][0]).imag < eval(list(sorted_results.items())[2][1][0]).imag
    else:
        assert True

def test_sort_results2(controller):
    if len(controller.results.keys()) > 1:
        sorted_results = controller.sort_results("real")
        assert eval(list(sorted_results.items())[0][1][0]).real < eval(list(sorted_results.items())[1][1][0]).real
        assert eval(list(sorted_results.items())[1][1][0]).real < eval(list(sorted_results.items())[2][1][0]).real
    else:
        assert True


def test_sort_results3(controller):
    if len(controller.results.keys()) > 1:
        sorted_results = controller.sort_results("date")
        assert list(sorted_results.items())[0][1][1] <= list(sorted_results.items())[1][1][1]
        assert list(sorted_results.items())[1][1][1] <= list(sorted_results.items())[2][1][1]
    else:
        assert True


def test_filer_result1(controller):
    controller.results = {'1+1j + 4+6j': ('(1+2j)', '17/05/2020'),
                          '1+4j * 8+5j': ('(5+37j)', '17/05/2020'),
                          '1+5j * 8+5j': ('(3+37j)', '17/05/2020'),
                          '1+7j - 7+5j': ('(7+20j)', '17/05/2020')}
    result = controller.filer_results(">", 5, "real")
    assert result == {'1+7j - 7+5j': ('(7+20j)', '17/05/2020')}


def test_filer_result2(controller):
    controller.results = {'1+1j + 4+6j': ('(1+1j)', '17/05/2020'),
                          '1+4j * 8+5j': ('(5+3j)', '17/05/2020'),
                          '1+5j * 8+5j': ('(3+5j)', '17/05/2020'),
                          '1+7j - 7+5j': ('(7+19j)', '17/05/2020')}
    result = controller.filer_results(">", 15, "imag")
    assert result == {'1+7j - 7+5j': ('(7+19j)', '17/05/2020')}


def test_filer_result3(controller):
    controller.results = {'1+1j + 4+6j': ('(1+1j)', '17/05/2020'),
                          '1+4j * 8+5j': ('(5+3j)', '17/05/2020'),
                          '1+5j * 8+5j': ('(3+5j)', '17/05/2020'),
                          '1+7j - 7+5j': ('(7+19j)', '17/05/2020')}
    result = controller.filer_results("==", 1, "imag")
    assert result == {'1+1j + 4+6j': ('(1+1j)', '17/05/2020')}


def test_filer_result4(controller):
    controller.results = {'1+1j + 4+6j': ('(1+1j)', '17/05/2020'),
                          '1+4j * 8+5j': ('(5+3j)', '17/05/2020'),
                          '1+5j * 8+5j': ('(3+5j)', '17/05/2020'),
                          '1+7j - 7+5j': ('(7+19j)', '17/05/2020')}
    result = controller.filer_results("<", 3, "real")
    assert result == {'1+1j + 4+6j': ('(1+1j)', '17/05/2020')}