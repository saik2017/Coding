# Uses python3
import sys
import random

def merge(a,b):
    c=[]
    count=0
    i,j=0,0
    while (i<len(a)) and (j<len(b)):
        if a[i]<=b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
            count+=(len(a)-i)
    if i<len(a):
        c=c+a[i:]
    else:
        c=c+b[j:]
    return (count,c)

def mergeSort(a,left,right):
    count=0
    if right-left==1:
        return (0,[a[left]])
    else:
        mid=int((left+right)/2)
        m,l1=mergeSort(a,left,mid)
        n,l2=mergeSort(a,mid,right)
        p,l=merge(l1,l2)
        count=(m+n+p)
        return (count,l)



def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    number_of_inversions,l=mergeSort(a,left,right)

    return number_of_inversions



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))


# def test(n):
#     a=[]
#     for i in range(n):
#         a.append(random.randint(1,10))
#     print(a)
#     p,l=mergeSort(a,0,n)
#     print(p)
#     print(l)


#test(8)