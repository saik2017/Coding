# Uses python3
import sys
import random


def partition3(a, l, r):
    #write your code here
    x = a[l]
    #print("The pivot is "+str(x))
    i=l
    for k in range(l+1,r+1):
        if a[k]<x:
            i+=1
            a[i],a[k]=a[k],a[i]
    a[l],a[i]=a[i],a[l]
    j=i
    for k in range(i+1,r+1):
        if a[k]==x:
            j+=1
            a[j],a[k]=a[k],a[j]
    return (i,j)



def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    y=a[k]
    a[l], a[k] = a[k], a[l]
    #use partition3
    m,n= partition3(a, l, r)
    randomized_quick_sort(a, l, m-1 )
    randomized_quick_sort(a, n + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
         print(x, end=' ')

def test(n):
    a=[]
    for i in range(n):
        a.append(random.randint(1,10))
    print(a)
    randomized_quick_sort(a,0,n-1)
    print(a)
#test(5)
#l=[7,2,10,1,5,5,10,7,7,5]
#print(partition3(l,0,9))
#print(l)
# randomized_quick_sort(l,0,9)
# print(l)
"""
Issues Faced :
Made wrong assumption of 2-partition
"""