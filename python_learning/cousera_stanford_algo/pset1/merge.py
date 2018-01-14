
NUMBERLIST_FILENAME = "G:/6.00.1x/coursera/pset1/numbers.txt"




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


def count_inversions():
    """
    counts the number of inversions in a array using merge sort
    """
    l=loadNumbers() #list of numbers
    global count
    count=0
    s=merge_sort(l)
    return  count
    
def merge_sort(l):
    n=len(l)
    if n==1:
        return l
    else:
        l1=merge_sort(l[:n/2])
        l2=merge_sort(l[n/2:])
        return merge(l1,l2)


def merge(l1,l2):
    l=[]
    i=0
    j=0
    while i<len(l1) and j<len(l2):
        if l1[i]<=l2[j]:
            l.append(l1[i])
            i+=1
        else:
            l.append(l2[j])
            j+=1
            global count
            count+=len(l1)-i    
    if i==len(l1):
        l.extend(l2[j:])
    if j==len(l2):
        l.extend(l1[i:])
                    
    return l          

        