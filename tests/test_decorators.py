# tests/test_decorators.py

from basics.decorators import logger, timer, square


def test_logger():
    @logger
    def greet():
        return "Hello"

    assert greet() == "Function greet executed"


def test_timer():
    @timer
    def fast_function():
        return "done"

    execution_time = fast_function()
    assert execution_time >= 0


def test_require_positive():
    assert square(4) == 16
    assert square(-3) == "Number must be positive"