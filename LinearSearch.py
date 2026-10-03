import random

l1 = [random.randint(0,9) for _ in range(10)]

def linear_search(l1, element):
    for i in l1:
        if i==element:
            return True
    return False

answer = linear_search(l1,12)
print(answer)
