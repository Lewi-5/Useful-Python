from typing import *

# we want to check if all the items are below a given upper bound
# inspired by solutions to this codewars problem: Small enough? - Beginner
# https://www.codewars.com/kata/57cc981a58da9e302a000214/solutions/python
nums: List[int] = [78, 117, 110, 99, 104, 117, 107, 115]

limit: int = 100

all_elems_smaller_than_limit: bool = all(elem < limit for elem in nums)

print(all_elems_smaller_than_limit) # prints False, as some elems are larger than limit

# or you could do the same with the any function

any_elem_larger_or_eq_to_limit: bool = any(elem >= limit for elem in nums)

print(any_elem_larger_or_eq_to_limit) # prints True, as there are elems larger or equal to limit


