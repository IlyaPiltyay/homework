
from src.decorators import my_function

def test_log_result(capsys):
    def my_function(x,y):
        return x + y
    result = my_function(1,2)
    assert result == 3



def test_log(capsys):
    filename = "mylog.txt"
    with open(filename, 'r', encoding='utf-8') as file:
        assert "my_function ok. Result: 3" in file.read()


def test_log_error(capsys):
    filename = "mylog.txt"
    with open(filename, 'r', encoding='utf-8') as file:
        if my_function(1, '2'):
            assert "my_function error - unsupported operand type(s) for +: 'int' and 'str'.Input (1, '2'),{}" in file.read()
