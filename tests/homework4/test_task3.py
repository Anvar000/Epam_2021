from homework4.task_3_get_print_output import my_precious_logger


def test_positive_out(capsys):
    my_precious_logger("Error: print")
    captured = capsys.readouterr()
    assert captured.out == "Error: print"
    assert captured.err == ""


def test_positive_err(capsys):
    my_precious_logger("error:not found")
    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == "error:not found"
