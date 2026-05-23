# from math_pkg.arithmetic import add is same as
from math_pkg.arithmetic import *

# using alias
import math_pkg.arithmetic as ar

# import specific function
from math_pkg.arithmetic import multiply


print(add(10,20))
print(ar.subtract(10,20))