import sys

try:
    print(f"My name is {sys.argv[1]}")
except IndexError as e:
    print("Argument not found")