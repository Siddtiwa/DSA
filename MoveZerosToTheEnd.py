l1 = [0,1,4,0,5,2]

i = 0
j = 0

while j < len(l1):
    if l1[i] == 0 and l1[j] != 0:
        l1[i] = l1[j]
        l1[j] = 0
    elif l1[i] != 0 and l1[j] == 0:
        