l1 = [1,2,3,4,5,6]
l2 = [1,2,7]

def Union(l1, l2):
    l3 = []
    i = 0
    j = 0
    while i<len(l1) and j<len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i+=1
        elif l1[i] > l2[j]:
            l3.append(l2[j])
            j+=1
        else:
            l3.append(l1[i])
            i+=1
            j+=1
    if i < len(l1):
        while i < len(l1):
            l3.append(l1[i])
            i+=1
    if j < len(l2):
        while j < len(l2):
            l3.append(l2[j])
            j+=1
    return l3

l3 = Union(l1,l2)

print(l3)