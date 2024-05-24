PI = 3.1416
GRAVITY = 9.8

def get_extensions(file):
    return file[file.index(".") +1:]

def get_filename(file):
    return file[:file.index(".")]

def righest_number(numbers):
    return max(numbers)
