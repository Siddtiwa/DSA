import random
import sys

l1 = [random.randint(0,99) for _ in range(10)]

def SecondLargest(l1):
    val = -sys.maxsize - 1
    val2 = -sys.maxsize - 1
    for i in l1:
        val = max(i, val)
    for i in l1:
        if i < val:
            val2 = max(i, val2)
    return val2

second_largest = SecondLargest(l1)

print(l1)
print(second_largest)
        