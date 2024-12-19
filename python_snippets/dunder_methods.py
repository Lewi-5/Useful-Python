from typing import *

# calls the greater than or equal dunder method on the limit value and passes each element from list a as arguments
def small_enough(a,l):
    return a==[*filter(l.__ge__,a)]
