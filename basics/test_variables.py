#python variables
#int Integer
#float floating point nos
#str String
#bool True or False
#list, tuple,dict, set for collection of data

def test_variable_assignments():
    name = "Shanet"
    age = 28
    place = "Mattathipara"
    salary = 10.5
    print("Name: ",name)
    print("Type of Name : ",type(name))


#function call
test_variable_assignments()

def test_typecast():
    empid = "156"
    converted_empid = int(empid)
    print(empid)
    print(f"conveted type {type(converted_empid)}")

test_typecast()

def test_callenge():
    api_response_time = "250"   # ms (string)

    response_time_ms = int(api_response_time)
    response_time_sec = response_time_ms / 1000

    print(f"API response time: {response_time_sec} seconds")
    

test_callenge()
