from typing import *




lst: List[int] = [5, 6, 7, 8, 9, 10, 11, 12]

first_iter: Iterator[int] = iter(lst)

print(f"first iter: {next(first_iter)}")

second_iter: Iterator[int] = iter(lst)
print(f"second iter: {next(second_iter)}")


print("moving first iter")
next(first_iter)

print(f"first iter: {list(first_iter)[0]}")
print(f"second iter: {list(second_iter)[0]}")

# another interesting way of doing the check no elems above limit question
# what is interesting here is that the first argument passed to the next
# function is not a case of list comprehension, notice the parentheses
# and no square brackets. This is creating a generator not a list! So this
# is a case of a generator expression/generator comprehension:
def small_enough(array, limit):
    return next((False for i in array if i > limit), True)