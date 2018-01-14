NUMBERLIST_FILENAME = "dijkstraData.txt"


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
        rows=[]
        values=map(str,line.split())
        for i in range(len(values)):
            temp=[]
            for j in values[i].split(','):
                temp.append(int(j))
                
            rows.append(temp)
                
        numberList.append(rows)
    print "  ", len(numberList), "numbers loaded."
           
    return numberList
    
def is_edge(L,a,b):
    if a>b:
        a,b=b,a
    for i in range(len(L)):    
        if L[i][0][0]==a:
            break
    for j in range(1,len(L[i])):
        if L[i][j][0]==b:
            return True
    return False           
        
 
def dist(L,a,b):
    if a>b:
        a,b=b,a
    for i in range(len(L)):    
        if L[i][0][0]==a:
            break
    for j in range(1,len(L[i])):
        if L[i][j][0]==b:
            return L[i][j][1]
        
def list_edges(L,a):
    for i in range(len(L)):    
        if L[i][0][0]==a:
            break
    l=[]
    for j in range(1,len(L[i])):
        l.append(L[i][j][0])
        
    for j in range(i):
        for k in range(len(L[j])):
            if L[j][k][0]==a:
                l.append(L[j][0][0])
    return l            
                    
def shortest_path(L):
    n=len(L)
    queue=[]
    seen=[]
    d={}
    set_value=1000000
    distance=1000000
    queue.append(1)
    while(queue!=[]):
        set_value=1000000
        node=queue.pop(0)
        if node==1:
            d[1]=0
            seen.append(node)
            edges=list_edges(L,node)
            queue.extend(edges)
            
            
        else:
            for j in seen:
                if is_edge(L,j,node)==True:
                    distance=d[j]+dist(L,j,node)
                    if distance<set_value:
                        set_value=distance   
            d[node]=set_value
            seen.append(node)
            edges=list_edges(L,node)
            for i in edges:
                if i not in queue and i not in seen:
                    queue.append(i)
            
                        
    for i in range(1,n+1):
        if i not in seen:
            d[i]=1000000        
            
                
    return d                    

L=loadNumbers()
#print L
o=shortest_path(L)
#print o
l=[]
for i in [7,37,59,82,99,115,133,165,188,197]:
    l.append(o[i])
print l