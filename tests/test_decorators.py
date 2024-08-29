

import pytest
from src.decorators import my_function,log

def test_log():
    def my_function(x,y):
        return x + y
    result = my_function(1,2)
    assert result == 3

def test_log_two(capsys):
    with pytest.raises(Exception):
        my_function()

def test_log_tree(capsys):
    @log(filename="")
    def my_function(x,y):
        return x + y
    my_function(1,2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok.\n"





