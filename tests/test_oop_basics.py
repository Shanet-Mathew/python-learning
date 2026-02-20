# tests/test_oop_basics.py

from basics.oop_basics import Student, BankAccount


def test_student_pass():
    student = Student("Shanet", 80)
    assert student.is_passed() is True


def test_student_grade():
    student = Student("John", 92)
    assert student.get_grade() == "A"


def test_bank_deposit():
    account = BankAccount("Shanet", 100)
    assert account.deposit(50) == 150


def test_bank_withdraw():
    account = BankAccount("Shanet", 100)
    assert account.withdraw(30) == 70


def test_bank_insufficient():
    account = BankAccount("Shanet", 100)
    assert account.withdraw(200) == "Insufficient funds"
