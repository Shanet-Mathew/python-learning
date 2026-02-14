#As it doesnt have test functions pytest will not work so run using : python tests/test_dictionary_set.py


# ----------------------------
# Task 1: Dictionary of Students
# ----------------------------

students = {
    "John": 85,
    "Alice": 92,
    "Bob": 76
}

print("All Students:")
for name, marks in students.items():
    print(name, ":", marks)


# ----------------------------
# Task 2: Students scoring more than 80
# ----------------------------

print("\nStudents scoring more than 80:")
for name, marks in students.items():
    if marks > 80:
        print(name, "-", marks)


# ----------------------------
# Task 3: Set Operations
# ----------------------------

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nCommon Numbers (Intersection):")
print(set1.intersection(set2))

print("\nAll Unique Numbers (Union):")
print(set1.union(set2))
