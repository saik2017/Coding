import pylab

inFile=open('julyTemps.txt','r',0)
high=[]
low=[]
for line in inFile:
    fields=line.split()
    if len(fields)!=3 or fields[0]=='Boston' or  fields[0]=='Day':
        pass
    else:
        fields=map(int,fields)
        high.append(fields[1])
        low.append(fields[2])
pylab.plot(low,high,'ro')
pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperature Ranges')

pylab.show()
    
    