import sys

from saying import *

if len(sys.argv) == 2:
    hello(sys.argv[1])
    goodbye(sys.argv[1])