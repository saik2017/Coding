#Uses python3

import sys

def largest_number(a):
    #write your code here
    res = ""
    while not a==[]:
        max_num=a[0]
        for x in a:
            if IsGreaterOrEqual(x,max_num):
                max_num=x
        a.remove(max_num)
        res+=str(max_num)

    return res


def IsGreaterOrEqual(x,y):
    x=str(x)
    y=str(y)
    if int(str(x)+str(y))>=int(str(y)+str(x)):
        return True
    else:
        return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
