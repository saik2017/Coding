NUMBERLIST_FILENAME = "graph.txt"


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
    return l            
                    


def shortest_path(L):
    """
    returns a dictionary of nodes as keys and shortes distance from node 1 as values
    """
    n=len(L)
    d={}
    seen=[]
    set_value=1000000
    distance=1000000
    d[1]=0
    seen.append(1)
    for k in range(1,n+1):
        if k in seen:
            for i in list_edges(L,k):
                if i not in seen:
                    distance=1000000
                    set_value=1000000
                    for j in seen:
                        if is_edge(L,j,i)==True:
                            distance=d[j]+dist(L,j,i)
                            if distance<set_value:
                                set_value=distance   
                    d[i]=set_value
                    seen.append(i)
        if k not in seen:
            distance=1000000
            set_value=1000000
            for j in seen:
                set_value=1000000
                if is_edge(L,j,k)==True:
                    distance=d[j]+dist(L,j,k)
                    if distance<set_value:
                        set_value=distance
            d[k]=set_value
            seen.append(k)
    print seen                     
    return d        
                            
                

        
                                
                    
        
L=loadNumbers()
#print L

o=shortest_path(L)
print o
l=[]
#for i in [7,37,59,82,99,115,133,165,188,197]:
#    l.append(o[i])
#print l    
                 
                           
                                        
                                                     
                                                                  
                                                                               
                                                                                            
                                                                                                                      
    
    
    
    
