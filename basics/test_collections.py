def test_lists():
	fruits = ["apple", "banana", "orange"]

	print(fruits)
	print(fruits[0])
	print(fruits[1:3])

	fruits.append("mango")
	fruits.remove("banana")

	for fruit in fruits:
		print(fruit)

def test_tuple():
	coordinates = (10, 20)

	print(coordinates)
	print(coordinates[0])

	# coordinates[0] = 5  # This will cause an error (immutability)

def test_dictionaries():
	person = {
    	"name": "Shanet",
    	"age": 28,
    	"city": "Mattathipara"
	}

	print(person["name"])
	print(person.get("age"))

	person["age"] = 29
	person["job"] = "Software Engineer"

	for key, value in person.items():
		print(f"{key}: {value}")
		
def test_sets():
	numbers = {1, 2, 3, 3, 2}

	print(numbers)

	numbers.add(4)
	numbers.remove(1)

	print(numbers)
