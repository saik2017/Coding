NUMBERLIST_FILENAME = "G:/6.00.1x/coursera/pset2/numbers2.txt"




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
        numberList.append(int(line.strip()))
    print "  ", len(numberList), "numbers loaded."
           
    return numberList

def count_comparisions():
    """
    counts the number of inversions in a array using merge sort
    """
    l=loadNumbers() #list of numbers
    global count
    count=0
    n=len(l)
    s=quickSort(l,0,n-1)
    return count


def quickSort(A,p,q):
    if p<q:
        global count
        count+=(q-p)
        l=q-p+1
          
        if l%2==0:
            i=(l/2)-1+p
            piv_list=[A[p],A[q],A[i]]
            piv_list.sort()
            piv=piv_list[1]
        elif l%2==1:
            i=(l/2)+p
            piv_list=[A[p],A[q],A[i]]
            piv_list.sort()
            piv=piv_list[1]
        
        piv=A[q]        
        r=Partition(A,p,q,piv)
        quickSort(A,p,r-1)
        quickSort(A,r+1,q)
    return A
  
    
def Partition(A,l,r,p):
    """
    partitions the arary A between the indices l and r around the pivot p
    
    """
    i=A.index(p)
    temp=A[l]
    A[l]=p
    A[i]=temp
    i=l+1
    
    for j in range(l+1,r+1):
        if A[j]<p:
            temp=A[i]
            A[i]=A[j]
            A[j]=temp
            i+=1
            
    A[l]=A[i-1]
    A[i-1]=p
   
    return (i-1)
           
    

    