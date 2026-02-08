def test_str():
	name = "Shanet"
	city = "Mattathipara"

	print(name)
	print(name[0])
	print(name[-1])
	print(name[0:3])
	print(len(name))

	age = 28

	print(f"My name is {name} and I am {age} years old")
	print("My name is {} and I am {} years old".format(name, age))

	

def test_typecasting():
	age_str = "28"
	salary_str = "10.5"

	age_int = int(age_str)
	salary_float = float(salary_str)

	print(age_int + 2)
	print(salary_float + 5.5)
	print(type(age_int))
	print(type(salary_float))

def test_input_conversion():
    user_age = "28"   # simulated input
    user_age_int = int(user_age)

    assert user_age_int + 1 == 29

def test_boolean_casting():
	print(bool(0))
	print(bool(1))
	print(bool(""))
	print(bool("python"))