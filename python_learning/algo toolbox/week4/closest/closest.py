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


def split_distance(X,Y,d):
    split=[]
    l=len(Y)
    a=X[int(l/2)-1].x
    b=X[int(l/2)-1].y
    for i in range(l):
        if a-d<=Y[i].x<=a+d:
            split.append(Y[i])
    l=len(split)
    best=d

    if l>7:
        for i in range(l):
            t=min(i+8,l)
            for j in range(i+1,t):
                s=split[i].distance(split[j])
                if s<best:
                    best=s

    if l<=7:
        for i in range(l):
            for j in range(i+1,l):
                s=split[i].distance(split[j])
                if s<best:
                    best=s

    #print(best)
    #print('______________________')
    return best


def minimum_distance(a, b):
    l=len(a)
    dummy={}
    s=list(set(a))

    X=[]
    Y=[]
    if len(s)<l/10:
        a,b=b,a
    for i in range(l):
        dummy[(a[i],b[i])]=0
    dummy=list(dummy.keys())
    if len(dummy)<l:
        return 0

    for i in dummy:
        X.append(Point1(i[0],i[1]))
        Y.append(Point2(i[0],i[1]))
    X.sort()
    Y.sort()
    return closest(X,Y)

def closest(PX,PY):
    if len(PX)<=1:
        return 0
    if len(PX)==2:
        return PX[0].distance(PX[1])
    elif len(PX)==3:
        d1=PX[0].distance(PX[1])
        d2=PX[0].distance(PX[2])
        d3=PX[1].distance(PX[2])
        return min(d1,d2,d3)
    l=len(PX)
    a=PX[int(l/2)].x
    b=PX[int(l/2)].y
    QX=PX[0:int(l/2)]
    RX=PX[int(l/2):]
    QY,RY=[],[]
    l=len(PY)
    for i in range(l):
        if PY[i].x<a:
            QY.append(PY[i])
        elif PY[i].x==a and PY[i].y<b:
            QY.append(PY[i])
        else:
            RY.append(PY[i])
    d1=closest(QX,QY)
    d2=closest(RX,RY)
    d=min(d1,d2)
    d3=split_distance(PX,PY,d)

    return min(d,d3)


def naive_closest(a,b):
    pts=[]
    for i in range(len(a)):
        pts.append(Point1(a[i],b[i]))
    d=pts[0].distance(pts[1])
    for i in range(len(pts)):
        for j in range(i+1,len(pts)):
            s=pts[i].distance(pts[j])
            if s<d:
                d=s
    return d



# if __name__ == '__main__':
#     input = sys.stdin.read()
#     data = list(map(int, input.split()))
#     n = data[0]
#     a = data[1::2]
#     b = data[2::2]
#     print("{0:.9f}".format(minimum_distance(a, b)))
#


def test():
    a=[]
    b=[]
    x,y=0,0
    while x==y:
        a,b=[],[]
        for i in range(25):
            a.append(random.randint(0,10))
            b.append(random.randint(0,10))

        x=naive_closest(a,b)
        y=minimum_distance(a,b)

    print(a)
    print(b)
    print(naive_closest(a,b))
    print(minimum_distance(a,b))

#test()
def test2(n):
    a, b = [], []
    for i in range(n):
        #a.append(5)
        #b.append(10**7)
        a.append(random.randint(-(10**9), 10**9))
        b.append(random.randint(-(10**9), 10**9))
    start=time.time()
    minimum_distance(a,b)
    end=time.time()
    if end-start>8:
        print(a)
        print(b)
    print(end-start)

#test2(100000)
def test3():
    start=time.time()
    end=time.time()
    while end-start<=8:
        start=time.time()
        test2(100000)
        end=time.time()


test3()
# a=[3,6,2,5,2,4,4,6]
# b=[0,8,6,2,4,6,7,6]
# print(minimum_distance(a,b))
