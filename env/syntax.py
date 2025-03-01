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
# - Mutable: can be modified after creation (add, remove, change items)
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
# - Mutable: can add, remove, or change key-value pairs