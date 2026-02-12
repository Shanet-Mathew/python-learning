def check_even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


def check_number_type(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    return "Zero"


def largest_number(a, b):
    return a if a > b else b


def login(username, password):
    correct_username = "admin"
    correct_password = "1234"
    if username == correct_username and password == correct_password:
        return "Login Successful"
    return "Invalid Credentials"
