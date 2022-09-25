import sys

try:
    if len(sys.argv) < 2:
        raise Exception("Argument count should be more than 1")
except Exception as e:
    print(e.args[0])

# 0번째 index를 제외한 나머지로 대체한다
sys.argv = sys.argv[1:]
for i,j in enumerate(sys.argv,start=1):
    print(f"Argument {i} : {j}")