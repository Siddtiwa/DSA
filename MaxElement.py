import random
import sys
l1 = [random.randint(0,99) for _ in range(10)]
def MaxElement(l1):
    val = -sys.maxsize - 1
    for i in l1:
        val = max(val, i)
    return val
max_element = MaxElement(l1)
print(max_element)
print(l1)