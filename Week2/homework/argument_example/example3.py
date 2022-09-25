import sys

name = "Default Name"
try:
    name = sys.argv[1]
except IndexError:
    pass

print(f"My name is {name}")