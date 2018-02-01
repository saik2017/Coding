import random
import matplotlib.pyplot as plt
class Location(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def move(self,deltaX,deltaY):
        """
        Moves a drunk from curren location to a new location.
        :param deltaX:  x direction displacement from current location.
        :param deltaY: y direction displacement from current location.
        :return: returns a new location with the final destination.
        """
        return Location(self.getX()+deltaX,self.getY()+deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self,other):
        return ((self.getX()-other.getX())**2+(self.getY()-other.getY())**2)**0.5

    def __str__(self):
        return '<'+str(self.getX())+','+str(self.getY())+'>'

class Field(object):
    def __init__(self):
        #Field contains a dictionary that maps drunks to their locations and is initially empty.
        self.drunks={}

    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError("Duplicate drunk")
        else:
            self.drunks[drunk]=loc

    def getLoc(self,drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")

        return self.drunks[drunk]

    def moveDrunk(self,drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        x,y=drunk.takeStep()
        current_location=self.drunks[drunk]
        self.drunks[drunk]=current_location.move(x,y)


class Drunk(object):
    def __init__(self,name):
        self.name=name

    def __str__(self):
        return "This drunk is named"+(self.name)

class UsualDrunk(Drunk):
    def takeStep(self):
        stepchoices=[(0.0,1.0),(0.0,-1.0),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepchoices)

class ColdDrunk(Drunk):
    def takeStep(self):
        stepChoices=[(0.0,0.9),(0.0,-1.1),(1.0,0.0),(-1.0,0.0)]
        return random.choice(stepChoices)


class styleIterator(object):
    def __init__(self,styles):
        self.index=0
        self.styles=styles

    def nextStyle(self):
        result=self.styles[self.index]
        if self.index==len(self.styles)-1:
            self.index=0
        else:
            self.index+=1
        return result




def walk(f,d,numSteps):
    """
    Simulates a single walk consisting of numSteps steps.
    :param f: is an instance of Field object.
    :param d: is an instance of drunk Object
    :param numSteps: Number of steps to be taken
    :return: distance of the drunk from starting point after the walk
    """
    initial=f.getLoc(d)
    for i in range(numSteps):
        f.moveDrunk(d)
    return initial.distFrom(f.getLoc(d))

def simwalks(numSteps,numTrials,dClass):
    """
    simulates a walk of numSteps steps for a numTrials times.
    :param numSteps: number of steps for each walk
    :param numTrials: number of walks
    :param dClass:Any subclass of Class Drunk
    :return distances: a List of distances of drunk from starting point after each trial
    """
    homer=dClass('')
    origin=Location(0,0)
    distances=[]
    for i in range(numTrials):
        f=Field()
        f.addDrunk(homer,origin)
        distances.append(round(walk(f,homer,numSteps),1))
    return distances

def simDrunk(numTrials,dClass,walkLengths):
     """
     Peforms a  num trials simulations for different walk lengths and prints the mean
     distance ,maximum distance and minimum distance from starting point.
     :param walkLengths: a list of numSteps
     :param numTrials:  num of trials of each walk of numsteps
     :param dClass: subclass of Drunk
     :return: a lit of mean distance from origin for different walk lengths
     """
     meanDistances=[]
     for numSteps in walkLengths:
         print("Simulation starting of",numSteps,"steps")
         trials=simwalks(numSteps,numTrials,dClass)
         print(dClass.__name__,'Random walk of',numSteps,'steps')
         print('mean=',round(sum(trials)/len(trials),4))
         print('max=',max(trials),'min=',min(trials))
         mean=sum(trials)/len(trials)
         meanDistances.append(mean)

     return meanDistances

def simAll(drunkKinds,walkLengths,numTrials):
    styleChoice=styleIterator(('m-','b--','g-'))
    for dClass in drunkKinds:
        curStyle=styleChoice.nextStyle()
        print('Starting simulation',dClass.__name__)
        means=simDrunk(numTrials,dClass,walkLengths)
        plt.plot(walkLengths,means,curStyle,label=dClass.__name__)
    plt.title("Mean distance from origin ("+str(numTrials)+' trials )')
    plt.xlabel('Number of steps')
    plt.ylabel('Distance from origin')
    plt.legend(loc='best')
    plt.show()





random.seed(0)
#drunktest([10,100,1000,10000],100,UsualDrunk)



drunkKinds=(UsualDrunk,ColdDrunk)
simAll(drunkKinds,[10,100,1000,10000],100)
