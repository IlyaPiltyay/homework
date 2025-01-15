from src.decorators import log


def test_log():
    def my_function(x, y):
        return x + y

    result = my_function(1, 2)
    assert result == 3


def test_log_tree(capsys):
    @log(filename="")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok.\n"


def test_path_file():
    @log(filename="file.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open("file.txt", "r") as file:
        out = file.read()
        assert out == "my_function ok"
