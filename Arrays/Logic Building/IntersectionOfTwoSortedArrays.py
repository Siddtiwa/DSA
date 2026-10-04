l1 = [1, 2, 2, 3, 3, 3]
l2 = [2, 3, 3, 4, 5, 7]

def Intersection(l1, l2):
    i = 0
    j = 0
    l3 = []
    while i<len(l1) and j<len(l2):
        if l1[i] == l2[j]:
            l3.append(l1[i])
            i+=1
            j+=1
        elif l1[i] > l2[j]:
            j+=1
        else:
            i+=1
    return l3

l3 = Intersection(l1,l2)

print(l3)