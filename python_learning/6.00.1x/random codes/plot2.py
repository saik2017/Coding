import pylab

principal=1000
interest=0.05
years=20
values=[]
for i in range(years+1):
    values.append(principal)
    principal+=principal*interest
pylab.plot(range(years+1),values,'r',linewidth=10,label='Principal vs years')
pylab.legend(loc='upper left')
 

pylab.title("5% growth compunded annually",fontsize=25)
pylab.xlabel("years",fontsize=16)
pylab.ylabel('value',fontsize=20)        

pylab.show()   