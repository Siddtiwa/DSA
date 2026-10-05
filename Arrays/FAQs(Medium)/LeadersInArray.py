import sys
l1 = [5, 4, 3, 2, 1]

def find_leader(l1):
    leader_array = []
    i = len(l1) - 1
    max_element = -sys.maxsize
    while i >= 0:
        if l1[i] > max_element:
            leader_array.append(l1[i])
            max_element = l1[i]
        i -= 1
    return leader_array[::-1]

larray = find_leader(l1)

print(larray)


