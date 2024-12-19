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