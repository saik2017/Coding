# python3

import sys

n, m = map(int, sys.stdin.readline().split())
lines = list(map(int, sys.stdin.readline().split()))
rank = [1] * n
parent = list(range(0, n))
ans = max(lines)
L=[]

def getParent(table):
    global L

    # find parent and compress path
    if table in L:
        return parent[table]
    temp=table
    while parent[table]!=table:
        table=parent[table]
        #parent[table]=getParent(parent[table])
    while parent[temp]!=temp:
        temp=parent[temp]
        parent[temp]=parent[table]
        L.append(temp)


    return parent[table]


def merge(destination, source):
    global ans
    global L
    L=[]
    realDestination, realSource = getParent(destination), getParent(source)

    if realDestination == realSource:
        return False

    # merge two components
    # use union by rank heuristic 
    # update ans with the new maximum table size
    if rank[realDestination]>rank[realSource]:
        parent[realSource]=realDestination
        lines[realDestination]+=lines[realSource]

        
    else:
        if rank[realDestination]==rank[realSource]:
            rank[realSource]+=1
            lines[realDestination]+=lines[realSource]
            parent[realSource] = realDestination
        else:
            lines[realSource]+=lines[realDestination]
            lines[realDestination]=lines[source]
            parent[realSource]=realDestination

    ans=max(lines)
    return True


for i in range(m):
    destination, source = map(int, sys.stdin.readline().split())
    merge(destination - 1, source - 1)
    print(ans)

