import random

l1 = sorted([random.randint(0,5) for _ in range(9)])
print(l1)

def remove_duplicates(l1):
    if len(l1) == 1:
        return l1, 1 
    i = 0
    j = 1
    while j < len(l1):
        if l1[j] > l1[i]:
            l1[i+1] = l1[j]
            i += 1
        else:
            j += 1

    return l1, i+1

l2, k = remove_duplicates(l1)

print(l2)
print(k)