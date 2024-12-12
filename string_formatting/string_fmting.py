from typing import *

# TODO
# add section on ljust, rjust, center


"""
decimal length and char width
"""

# You can specify the number of decimal places in an f string interpolated float this way
# REMINDER THIS WILL ROUND

pi: float = 3.1415926535

pi_string: str = f"{pi:.4f}"

# print(pi_string) # 3.1416

height1: float = 1.985

height2: float = 1.984

height1_string: str = f"{height1:.2f}"
height2_string: str = f"{height2:.2f}"

# print(height1_string) # rounds up, prints 1.99
# print(height2_string) # rounds down, prints 1.98

# you can also specify the total char width, including the decimal point, you would like your float to extend
# floats shorter than the char width will be left padded with zeros, floats longer will not be truncated and will appear as if nothing happened

seconds: float = 5.4

# print(f"{seconds:06}") # prints 0005.4


# you can combine both char width and decimal length

degrees: float = 34.5639

print(f"{degrees:09.5f}") # prints 034.56390

"""
.zfill
"""

# you can fill your string with zeroes using .zfill

pizza_slices: str = "8"

pizza_slices4 = pizza_slices.zfill(4)

# print(pizza_slices4) # prints 0008


pizza_slices10 = pizza_slices.zfill(10)

# print(pizza_slices10) # prints 0000000008

pizza_slices24 = pizza_slices.zfill(24)


# print(pizza_slices24) # prints 000000000000000000000008




# you can pass comparisons which evaluate to boolean values as indexes to a string subscript:


introversion: int = -5

char: str = 'IE'

# we use the format method on a string and pass the index designated by the value of a boolean expression True = 1, False = 0
myers_briggs: str = "{}NTJ".format(char[introversion >= 0])

# print(myers_briggs) # prints INTJ

"""
percent specifier
"""

movie_ticket: float = 17.95

days: int = 89


hours: float = 1012.834

movie_sentence: str = "for %05d days I spent %07.3f per movie and watched a total of %09.2f hours" % (days, movie_ticket, hours)

# print(movie_sentence)


"""

"""


