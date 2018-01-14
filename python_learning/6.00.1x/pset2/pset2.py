"""Given a string in lowercase , we need to print
 out the largest substring which is in alphabetical order"""
s=raw_input("Enter any string in lowercase:")
print(len(s))
begin,end,start,stop,inseq=0,0,0,0,0
        # beginning index of largest substring in order
        # ending index of largest substring in order
        # temporary starting index of a substring in order
        # temporary ending index of string in order
for i in range(len(s)-1):
    if inseq==0:
        start,stop,inseq=i,i,1
    if s[i]<=s[i+1] and inseq==1:
        stop+=1
    if s[i]>s[i+1]:
        inseq=0
    if (stop-start)>end-begin and (inseq==0 or i+1==len(s)-1):
        begin=start
        end=stop
        print(begin,end)
print('The longest substring in alphabetical order is '+ s[begin:end+1])


