#Uses python3
import sys
import math
import random
import time

class Point1(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)

    def __lt__(self, other):
        if self.x==other.x:
            return self.y<=other.y
        return self.x<other.x

    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'



class Point2(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def distance(self,other):
        return math.sqrt((self.x-other.x)**2+(self.y-other.y)**2)

    def __lt__(self, other):
        if self.y==other.y:
            return self.x<=other.x
        return self.y<other.y

    def __str__(self):
        return '<'+str(self.x)+','+str(self.y)+'>'


def split_distance(split,d):
    l=len(split)
    best=d
    if l>7:
        for i in range(l-7):
            for j in range(i+1,i+8):
                s=split[i].distance(split[j])
                if s<best:
                    best=s

    elif l<=7:
        for i in range(l):
            for j in range(i+1,l):
                s=split[i].distance(split[j])
                if s<best:
                    best=s

    #print(best)
    #print('______________________')
    return best



def closest(X,Y):
    assert len(X)==len(Y)
    l=len(X)
    if len(X)<=1:
        return 0
    if len(X)==2:
        return X[0].distance(X[1])
    if len(X)==3:
        d1=X[0].distance(X[1])
        d2=X[0].distance(X[2])
        d3=X[1].distance(X[2])
        return min(d1,d2,d3)

    a=X[int(l/2)]
    X_left=X[0:int(l/2)]
    X_right=X[int(l/2):]
    Y_left,Y_right=[],[]
    for i in range(l):
        p=Point1(Y[i].x,Y[i].y)
        q=Point2(Y[i].x,Y[i].y)
        if p<a and len(Y_left)<int(l/2):
            Y_left.append(q)
        else:
            Y_right.append(q)

    # for i in X_left:
    #     print(i,end=' ')
    # print('---------')
    # for i in X_right:
    #     print(i,end=' ')
    # print('-------------')
    # for i in Y_left:
    #     print(i,end=' ')
    # print('------------')
    # for i in Y_right:
    #     print(i,end=' ')

    d1=closest(X_left,Y_left)
    d2=closest(X_right,Y_right)
    d=min(d1,d2)
    split = []
    l = len(Y)
    a = X[int(l / 2)-1].x
    for i in range(l):
        if a - d <= Y[i].x <= a + d:
            split.append(Y[i])
    return split_distance(split,d)


def minimum_distance(a, b):
    """

    :param a: list of x coordinates of the points
    :param b: list of y coordinates of the points
    :return: minimum distance
    """
    assert len(a)==len(b)
    l=len(a)
    # we use a dummy dict to check if there are any repeating points
    dummy = {}
    s = list(set(a))
    # if len(s) < l / 10:
    #     a, b = b, a

    for i in range(l):
        dummy[(a[i], b[i])] = 0

    dummy = list(dummy.keys())
    if len(dummy) < l:
        return 0
    X=[]
    Y=[]
    for i in range(len(a)):
        X.append(Point1(a[i],b[i]))
        Y.append(Point2(a[i],b[i]))
    X.sort()
    Y.sort()
    # for i in X:
    #     print(i, end='  ')
    # print('---------------')
    # for i in Y:
    #     print(i,end='  ')
    # print('*************')
    return closest(X,Y)

#minimum_distance([1,3,4,0,-1,6,5,-2,4],[-1,9,10,1,2,-1,4,0,-1])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1::2]
    b = data[2::2]
    print("{0:.9f}".format(minimum_distance(a, b)))


def test2(n):
    a, b = [], []
    for i in range(n):
        a.append(5)
        #b.append(10**7)
        #a.append(random.randint(-(10**9), 10**9))
        b.append(random.randint(-(10**9), 10**9))
    start=time.time()
    minimum_distance(a,b)
    end=time.time()
    if end-start>8:
        print(a)
        print(b)
    print(end-start)

#test2(100000)