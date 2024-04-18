"""
io.py
- Read input file and return parameter
"""

def parse_input_file():
    with open("../input/input.txt", "r") as file:
        # Get RSA algorithm version
        version = str(file.readline().strip())
        n = int(file.readline().strip())
        e = int(file.readline().strip())
        c = int(file.readline().strip())

    return version, n, e, c