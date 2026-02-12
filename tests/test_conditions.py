from basics.conditions import (
    check_even_or_odd,
    check_number_type,
    largest_number,
    login,
)


def test_even_number():
    assert check_even_or_odd(4) == "Even"


def test_odd_number():
    assert check_even_or_odd(5) == "Odd"


def test_positive_number():
    assert check_number_type(10) == "Positive"


def test_negative_number():
    assert check_number_type(-3) == "Negative"


def test_zero():
    assert check_number_type(0) == "Zero"


def test_largest_number():
    assert largest_number(10, 5) == 10


def test_login_success():
    assert login("admin", "1234") == "Login Successful"


def test_login_failure():
    assert login("user", "wrong") == "Invalid Credentials"
