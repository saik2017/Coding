import random


NUMBERLIST_FILENAME = "G:/6.00.1x/coursera/pset3/kargerMincut.txt"


def loadNumbers():
    """
    Returns a list of Numbers read from a file
    
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(NUMBERLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    numberList = []
    for line in inFile:
        values=map(int,line.split())
        numberList.append(values)
    print "  ", len(numberList), "numbers loaded."
           
    return numberList
    


def num_nodes(L):
    """
    returns the number of nodes  in the graph
    """
    l=[]
    for i in L:
        if i[0] not in l:
            l.append(i[0])
    return len(l)      
    
      
        
def choose_cut(L):
    """
    chooses a random min cut by selecting two nodes
    """
    n=len(L)
    i=random.randrange(n)   
    j=random.randrange(1,len(L[i]))
    s=L[i][j]
    for k in range(n):
        n1=len(L[k])
        for x in range(n1):
            if L[k][x]==s:
                L[k][x]=L[i][0]


def count_edges(L):
    """
    counts the number of edges in the graph
    """
    n=len(L)
    count=0
    for i in range(n):
        n1=len(L[i])
        for j in range(n1):
            if L[i][j]!=L[i][0]:
                count+=1
    count/=2
    
    return count            
            
def get_mincut():
    L=loadNumbers()
    dummy=L[:]
    v=num_nodes(L)
    mincut=100000
    iters=int(num_nodes(L))**1
    if v==2:
        return count_edges(L)
    while iters>0:
        v=num_nodes(L)
        while v>2:
            choose_cut(L)
            v=num_nodes(L)
        e=count_edges(L)
        print mincut
        if e<mincut:
            mincut=e
        iters-=1
        L=dummy
    return e    
            
            
    