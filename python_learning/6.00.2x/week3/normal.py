import scipy.integrate
import pylab
import random

def gaussian(x,mu,sigma):
    factor1=(1.0/(sigma*((2*pylab.pi)**0.5)))
    factor2=pylab.e**(-1*((x-mu)**2)/(2*(sigma**2)))
    return factor1*factor2



def checkEmperical(numTrials):
    for i in range(numTrials):
        mu=random.randint(-10,10)
        sigma=random.randint(1,10)
        print('For mu =',mu,'and sigma =',sigma)
        for num in [1,1.96,3.0]:
            area=scipy.integrate.quad(gaussian,mu-num*sigma,mu+num*sigma,(mu,sigma))[0]
            print("Fraction of area within "+str(num)+" standard deviations=",round(area,4))

checkEmperical(3)

