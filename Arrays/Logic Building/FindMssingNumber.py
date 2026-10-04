l1 = [0,1,2,3,4]
n = len(l1)

def FindTheMissingNumber(l1, n):
    sum = (n*(n+1))/2
    lsum = 0
    for i in l1:
        lsum += i
    return sum - lsum

missing_number = FindTheMissingNumber(l1,n)

print(n)

