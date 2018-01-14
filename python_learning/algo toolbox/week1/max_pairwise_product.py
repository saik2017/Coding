# Uses python3
n = int(input())
print(n)
a = [int(x) for x in input().split()]
print(a)
assert(len(a) == n)

result = 0
max1=0
max2=0
for i in range(0, n):
    if a[i]>max1:
        max2=max1
        max1=a[i]
    elif a[i]>max2:
        max2=a[i]
    else:
        continue
result=max1*max2
print(result)
