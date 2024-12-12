from typing import *

from math import * 

"""
modf function returns two values, first the fractional part of a float and then the whole number
"""

num: float = 100.12

rem: float
whole: float
rem, whole = modf(num)


# print(f"{rem:.3f}") # prints 0.120
# print(whole) # prints 100.0

# you can also get the fractional part of a float by using modulus 1

num2: float = 123.3434


print(num2 % 1) # prints .34340000