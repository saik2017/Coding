# Uses python3
import sys
#This can be solved in linear time using a dict and scanning the array twice.


def get_majority_element(a, left, right):
    count1,count2=0,0
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]

    mid=int((left+right)/2)

    left_major=get_majority_element(a,left,mid)
    right_major=get_majority_element(a,mid,right)
    # print(left_major)
    # print(right_major)
    # print('-------')
    if left_major==-1 and right_major==-1:
        return -1
    if left_major==right_major:
        return left_major
    for i in range(left,right):
        if a[i]==left_major:
            count1+=1
        if a[i]==right_major:
            count2+=1
    if max(count1,count2)<=int((right-left)/2):
        return -1
    if count1>count2:
        return left_major
    else:
        return right_major



if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)



