import sys

try:
    if len(sys.argv) < 3 or len(sys.argv) > 3:
        raise IndexError("Argument count not matched")
    _,name,age = sys.argv
    try:
        age = int(age)
    except ValueError as e:
        print("Argument type not matched")
        sys.exit()
    print(f"My name is {sys.argv[1]} and my age is {sys.argv[2]}")
except IndexError as e:
    print(e.args[0])