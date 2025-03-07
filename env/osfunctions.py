import os

cwd = os.getcwd()
print(f"Working Directory: {cwd}")

os.chdir('../')
cwd = os.getcwd()
print(f"Working Directory: {cwd}")

directory = "test"
parent_dir = "C:/Users/Reh06/pyworkshop/"
path = os.path.join(parent_dir, directory)

try:
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"Directory '{directory}' created")
    else:
        print(f"Directory '{directory}' already exists")
except Exception as e:
    print(f"Error creating directory: {e}")

nested_directory = "test/nested/subdirectory"
nested_path = os.path.join(parent_dir, nested_directory)

try:
    if not os.path.exists(nested_path):
        os.makedirs(nested_path)
        print(f"Nested directories '{nested_directory}' created")
    else:
        print(f"Nested directories '{nested_directory}' already exist")
except Exception as e:
    print(f"Error creating nested directories: {e}")

print("Directory structure created successfully!")


path2 = path
try:
    dir_list = os.listdir(path2)
    print(f"Files and Directories in '{path2}': ")
    for item in dir_list:
        print(f"{item}")
except PermissionError:
    print(f"Permission denied to list directory: {path2}")
except Exception as e:
    print(f"Error listing directory: {e}")

test_file = os.path.join(path, "temp_file.txt")
try:
    with open(test_file, 'w') as f:
        f.write("This is a temporary file for testing os.remove()")
    print(f"Created test file: {test_file}")
    
    os.remove(test_file)
    print(f"Successfully removed file: {test_file}")
except Exception as e:
    print(f"Error with file operations: {e}")

print(os.name)