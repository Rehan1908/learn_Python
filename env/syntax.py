
age = 20
if age >= 18:
  print("Eligible To vote")
print(f"Current age: {age}")

marks = 45
res = "Pass" if marks >= 40 else "Fail"
print(f"result: {res}")
print(f"Marks: {marks}")

x=12
y = 3 / 4
a = float(5)
name = "Nina"
print(f"Values: x={x}, y={y}, a={a}, name={name}")

print(type(x))
print(type(y))
print(type(a))
print(type(name))

dir_result = dir(name)
print(f"Directory result: {dir_result[:5]}...")

rent = 480
per_day = rent // 30
print(per_day)
print(f"Rent: {rent}")

print("My name is", name)
print(f"Name printed: {name}")

print("Hello, this is %s" %name)
print(f"Used string formatting")

print(f"Hello, my name is {name} and i pay ${rent // 30} in rent per day")
print(f"Used f-string formatting")

my_list = ['h','e','l','l','o']
print(my_list)
my_list.append('!')
print(my_list)

my_list.remove("l")
print(my_list)
my_list.insert(2, "l")
print(my_list)

del my_list[0]
print(my_list)
last_item = my_list.pop()
print(f"Popped: {last_item}")
print(my_list)
print(my_list[2])
print(f"Is '!' in list: {'!' in my_list}")
my_list.sort(reverse=True)
print(my_list)
sorted_result = sorted(my_list, reverse=False)
print(f"Sorted result: {sorted_result}")
print(my_list)

my_set = {}
print(type(my_set))
print(f"Empty dict created: {my_set}")

my_set = set()
print(type(my_set))
print(f"Empty set created: {my_set}")

my_set = {1, 2, 3}
print(f"Set created: {my_set}")
my_set.add(4)
print(my_set)
my_set.remove(2)
print(my_set)
print(f"Is 2 in my_set? {2 in my_set}")

print(my_set)
my_set.add(3)
print(my_set)

my_other_set = {1, 2, 3}
print(f"Other set: {my_other_set}")
print(f"Union: {my_set.union(my_other_set)}")
print(f"Intersection: {my_set.intersection(my_other_set)}")

my_tuple = 1,
print(my_tuple)
print(f"Created tuple: {my_tuple}")

person = ('Jim', 29, 'Austin, TX')
name, age, hometown = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Hometown: {hometown}")
print(f"Unpacked tuple successfully")

my_dict = {"key": "value"}
print(f"Created dictionary: {my_dict}")

my_dict["hello"] = "world"
print(my_dict)
my_dict["foo"] = "bar"
print(my_dict)
print(my_dict["hello"])
print(my_dict.get("hello"))
print(f"Accessed dictionary values")

print(f"Is 'baz' in my_dict? {'baz' in my_dict}")
print(my_dict.get("baz", "default response"))
print(f"Keys: {my_dict.keys()}")
print(f"Values: {my_dict.values()}")
print(f"Items: {my_dict.items()}")

my_list = [1, 2, 3]
print(my_list)
my_list[0] = 'a'
print(my_list)

my_dict = {"hello": "world"}
print(my_dict)
my_dict["foo"] = "bar"
print(my_dict)

my_set = {1, 2, 3}
print(my_set)
my_set.add('a')
print(my_set)

my_tuple = (1, 2, 3)
print(my_tuple)
print(f"Created immutable tuple: {my_tuple}")


for i in my_tuple:
  print(i)


  # ====================== PYTHON FUNCTIONS & CONTROL FLOW ======================

  # FUNCTIONS
  # - Reusable blocks of code defined with 'def' keyword
  # - Can accept parameters/arguments and return values
  # - Helps organize code and prevent repetition
  # - Can have default parameter values
  # - Supports positional and keyword arguments
  # - Local variables exist only within the function scope

  # CONDITIONALS (if-elif-else)
  # - Used for decision making in code
  # - Structure: if condition: code elif condition: code else: code
  # - Conditions evaluate to True or False
  # - Multiple conditions can be combined with 'and', 'or', 'not'
  # - Ternary operator: value_if_true if condition else value_if_false

  # LOOPS
  # - for loops: iterate over sequences (lists, tuples, strings, etc.)
  # - while loops: execute code as long as a condition is True
  # - break: immediately exits the loop
  # - continue: skips the current iteration and moves to the next one
  # - Nested loops: loops within loops for more complex iteration patterns

  # RETURN STATEMENTS
  # - Used to send values back from functions
  # - Can return one or multiple values (as a tuple)
  # - Function execution stops when return is reached
  # - If no return statement, function returns None implicitly

  # SCOPE
  # - Variables defined inside functions are local to that function
  # - Global variables are defined outside functions and accessible everywhere
  # - Python follows LEGB rule: Local, Enclosing, Global, Built-in

  # Basic Function Example
  def greet(name):
    return f"Hello, {name}!"

  greeting = greet("World")
  print(f"Function returned: {greeting}")

  # Conditionals Example
  temperature = 75
  if temperature > 80:
    weather = "It's hot!"
  elif temperature > 60:
    weather = "It's nice!"
  else:
    weather = "It's cold!"
  print(f"Weather condition: {weather}")

  # Ternary Operator Example
  time = 13
  period = "afternoon" if time >= 12 else "morning"
  print(f"Time period: {period}")

  # For Loop Example
  fruits = ["apple", "banana", "cherry"]
  print("Looping through fruits:")
  for fruit in fruits:
    print(f"- {fruit}")

  # While Loop Example
  count = 3
  print("Countdown:")
  while count > 0:
    print(f"- {count}")
    count -= 1
  print("Liftoff!")

  # Break Example
  print("Demo of break statement:")
  for i in range(10):
    if i == 5:
      print("Breaking the loop at 5")
      break
    print(f"Loop value: {i}")

  # Continue Example
  print("Demo of continue statement:")
  for i in range(5):
    if i == 2:
      print("Skipping 2")
      continue
    print(f"Loop value: {i}")

  # Multiple Return Values Example
  def get_dimensions():
    return 10, 20

  width, height = get_dimensions()
  print(f"Dimensions: {width}x{height}")

  # Scope Example
  global_var = "I'm global"

  def scope_demo():
    local_var = "I'm local"
    print(f"Inside function - Local: {local_var}")
    print(f"Inside function - Global: {global_var}")

  scope_demo()
  print(f"Outside function - Global: {global_var}")

def add_numbers(x, y):
    return x + y

print(f"the Sum of numbers 3 and 7 is {add_numbers(3,7)}")


def calculate_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
calculate_numbers(2, 3)
calculate_numbers(2, 3, "subtract")
calculate_numbers(2, 3, operation="subtract")


def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz!")
fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(15)


def my_func(my_list):
    if my_list:
        for item in my_list:
            if item is None:
                print("Got None!")
            else:
                print(item)
    else:
        print("Got an empty list!")
my_func([1, 2, 3])
my_func([2, None, "hello", 42])
my_func([])

my_list = [0, 1, 2]
for num in my_list:
    print(f"Next value: {num}")

for num in range(0, 3):
    print(f"Next value: {num}")


my_list = ["foo", "bar", "baz"]
for index, item in enumerate(my_list):
    print(f"Item {index}: {item}")

my_list = ["foo", "bar", "baz"]
for index, item in enumerate(my_list):
    print(f"Item {index}: {item}")

for value in my_dict.values():
    print(f"Value: {value}")

for key, value in my_dict.items():
    print(f"Item {key} = {value}")

def is_number_in_list(number_to_check, list_to_search):
    for num in list_to_search:
        print(f"Checking {num}...")
        if num == number_to_check:
            return True
    return False
my_list = [1, 2, 3, 4, 5]
is_number_in_list(27, my_list)
is_number_in_list(2, my_list)

counter = 0
while counter < 3:
    print(f"Counter = {counter}")
    counter += 1

names = ["Rose", "Max", "Nina"]
target_letter = 'x'
found = False

for name in names:
    for char in name:
            if char == target_letter:
                    found = True
                    break

    if found:
        print(f"Found {name} with letter: {target_letter}")
        break

for x in range(0, 5):
    for y in range(0, 5):
        print(f"x = {x}, y = {y}")
        if y == 2:
            break







# ====================== PYTHON DATA TYPES ======================

# INTEGER (int)
# - Whole numbers without decimal points (e.g., 20, 45, 12)
# - Operations: addition (+), subtraction (-), multiplication (*), division (/), floor division (//), modulo (%)
# - No size limit (can represent arbitrarily large numbers)
# - Immutable: once created, their value cannot be changed

# FLOAT (float)
# - Numbers with decimal points (e.g., 3/4 = 0.75, float(5) = 5.0)
# - Used for representing real numbers
# - Limited precision (may have rounding errors)
# - Immutable data type
# - Operations: same as integers plus additional floating-point operations

# STRING (str)
# - Sequence of characters enclosed in quotes (single ' ', double " ", or triple ''' ''')
# - Immutable: cannot be changed after creation
# - Operations: concatenation (+), repetition (*), slicing [:], methods like .upper(), .lower(), etc.
# - Supports indexing (name[0]) and iteration
# - F-strings (f"...{variable}...") provide easy string formatting

# LIST (list)
# - Ordered collection of items enclosed in square brackets []
# - Mutable: can be modified after creatio n (add, remove, change items)
# - Elements can be of different data types
# - Common methods: .append(), .remove(), .insert(), .pop(), .sort()
# - Supports indexing, slicing, and iteration
# - Can contain duplicate elements
# - Memory-efficient and dynamic in size

# SET (set)
# - Unordered collection of unique items enclosed in curly braces {}
# - Mutable: can add or remove items
# - No duplicate elements allowed
# - No indexing (since unordered)
# - Fast membership testing (x in set)
# - Set operations: union(), intersection(), difference(), symmetric_difference()
# - Empty set must be created with set(), not {} (which creates a dict)

# TUPLE (tuple)
# - Ordered, immutable collection of items enclosed in parentheses ()
# - Cannot be modified after creation
# - Can contain elements of different data types
# - Supports indexing and iteration
# - More memory efficient than lists
# - Can be used as dictionary keys (unlike lists)
# - Single-item tuples need a trailing comma: (1,)

# DICTIONARY (dict)
# - Collection of key-value pairs enclosed in curly braces {}
# - Keys must be unique and immutable (strings, numbers, tuples)
# - Values can be any data type and mutable
# - Unordered (before Python 3.7) or insertion-ordered (3.7+)
# - Access values using square brackets with key: dict[key]
# - Common methods: .get(), .keys(), .values(), .items()
# - Fast lookup by key
# - Mutable: can add, remove, or change key-value pairs'





my_list = [num for num in range(0,100) if num % 2 == 0]
print (my_list)

import random;

my_dict = {num:random.randint(0,10) for num in my_list}
print(my_dict)

my_set = {num for num in my_dict.values()}
print(my_set)

# List operations with print statements
my_list = ["h", "e", "l", "l", "o", "!"]
print(f"List created: {my_list}")
print(f"List length: {len(my_list)}")
print(f"Slice [4:6]: {my_list[4:6]}")
print(f"Slice [4:]: {my_list[4:]}")
print(f"Slice [-2:]: {my_list[-2:]}")

# Range and slicing operations
my_list = [num for num in range(0, 100)]
print(f"Created list with range (showing first 5): {my_list[:5]}...")
my_slice = my_list[30:70:2]
print(f"Slice from 30 to 70 with step 2 (showing first 5): {my_slice[:5]}...")
my_backwards_slice = my_slice[::-1]
print(f"Reversed slice (showing first 5): {my_backwards_slice[:5]}...")

# Zip operation with names and scores
names = ["Nina", "Max", "Floyd", "Lloyd"]
scores = [random.randint(0, 100) for name in names]
print(f"Generated scores: {scores}")
for name, score in zip(names, scores):
  print(f"{name} got a score of {score}")

# Type conversions
my_string = str(100)
print(f"Converted int to string: '{my_string}'")
print(f"Type of converted string: {type(my_string).__name__}")
my_int = int(my_string)
print(f"Converted back to int: {my_int}")
print(f"Type of converted int: {type(my_int).__name__}")

# More conversions
float_val = float("3.1415")
print(f"String to float: {float_val}")
int_val = int(3.1415)
print(f"Float to int (truncates): {int_val}")

# List and string conversions
my_list = list("hello")
print(f"String to list: {my_list}")
list_as_string = str(my_list)
print(f"List as string: {list_as_string}")

# Join operations
empty_join = ''.join(my_list)
print(f"Join with empty separator: {empty_join}")
comma_join = ','.join(my_list)
print(f"Join with comma separator: {comma_join}")
dash_join = '-'.join(my_list)
print(f"Join with dash separator: {dash_join}")

# Split operation
my_string = "the,quick,brown,fox"
split_result = my_string.split(",")
print(f"Original string: {my_string}")
print(f"Split string by comma: {split_result}")