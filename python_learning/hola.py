#print 'hello world'

class Person(object):
    def __init__(self, name):
        self.name = name
    def say(self, stuff):
        return self.name + ' says: ' + stuff
    def __str__(self):
        return self.name

class Lecturer(Person):
    def lecture(self, stuff):
        return 'I believe that ' + Person.say(self, stuff)

class Professor(Lecturer):
    def say(self, stuff):
        return self.name + ' says: ' + self.lecture(stuff)

class ArrogantProfessor(Professor):
    def lecture(self, stuff):
        return "It is obvious that "+Person.say(self,stuff)

    def say(self, stuff):
        return self.name+" says: "+self.lecture(stuff)


# e = Person('eric')
# le = Lecturer('eric')
# pe = Professor('eric')
# ae = ArrogantProfessor('eric')
# print(e.say('the sky is blue'))
# print(le.say('the sky is blue'))
# print(le.lecture('the sky is blue'))
# print(pe.say('the sky is blue'))
# print(pe.lecture('the sky is blue'))
# print(ae.say('the sky is blue'))
# print(ae.lecture('the sky is blue'))


class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self):
        """ initialization of your representation """
        # FILL THIS IN
        self.l=[]

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        # FILL THIS IN
        new=True
        for i in range(len(self.l)):
            if self.l[i][0]==k:
                self.l[i][1]=v
                new=False
        if new==True:
            self.l.append([k,v])



    def getval(self, k):
        """ k, immutable object  """
        # FILL THIS IN
        iselem=False
        for i in range(len(self.l)):
            if self.l[i][0]==k:
                iselem=True
                return self.l[i][1]
        if iselem==False:
            raise KeyError


    def delete(self, k):
        """ k, immutable object """
        # FILL THIS IN
        iselem=False
        for i in range(len(self.l)):
            if self.l[i][0]==k:
                iselem=True
                self.l=self.l[:i]+self.l[i+1:]
                break
        if iselem==False:
            raise KeyError

d1=myDict()
d1.assign(2,3)
#print(d1.getval(2))
d1.assign(3,9)
#print(d1.getval(3))
#print(d1.getval(2))
#d1.assign(4,2)

d1.delete(2)
#d1.delete(2)
#print(d1.getval(3))


