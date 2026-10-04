import random

#l1 = [random.randint(0,1) for _ in range(10)]
l1 = [1,1,0,0,1,1,1,0]

def MaxConsecutiveOnes(l1):
    global_count = 0
    local_count = 0
    for i in l1:
        global_count = max(global_count, local_count)
        if i == 1:
            local_count += 1
        else:
            local_count = 0
    return global_count

count = MaxConsecutiveOnes(l1)

print(l1)
print(count)
        