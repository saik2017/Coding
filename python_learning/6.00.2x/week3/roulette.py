import random

class FairRoulette(object):
    def __init__(self):
        self.pockets=[]
        for i in range(1,37):
            self.pockets.append(i)
        self.ball=None
        self.blackOdds=1.0
        self.redOdds=1.0
        self.pocketOdss=len(self.pockets)-1

    def spin(self):
        self.ball=random.choice(self.pockets)

    def isBalck(self):
        if type(self.ball)!=int:
            return False
        if 0<self.ball<=10 or 18<self.ball<=28:
            return self.ball%2==0
        else:
            return self.ball%2==1

    def isRed(self):
        return type(self.ball)==int and  not self.isBalck()

    def betBalck(self,amt):
        if self.isBalck():
            return amt*self.blackOdds
        return -amt

    def betRed(self,amt):
        if self.isRed():
            return amt*self.redOdds
        return -amt

    def betPocket(self,pocket,amt):
        if str(self.ball)==str(pocket):
            return amt*self.pocketOdss
        return -amt

    def __str__(self):
        return "Fair Roulette"

class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append('0')

    def __str__(self):
        return "European roulette"

class AmRouletter(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append('00')

def playRoulette(game,numSpins):
    bet_number=2
    bet=1.0
    toPocket,toRed,toBalck=0.0,0.0,0.0
    for i in range(numSpins):
        game.spin()
        toPocket+=game.betPocket(bet_number,bet)
        toRed+=game.betRed(bet)
        toBalck+=game.betBalck(bet)

    print(str(numSpins) +' spins of '+str(game))
    print('Expected return betting red  = '+str(100*toRed/numSpins)+'%')
    print("Expected return betting balck = "+str(100*toBalck/numSpins)+'%')
    print("Expected return betting pocket 2 = "+str(100*toPocket/numSpins)+'%')

    return

playRoulette(FairRoulette(),1000000)
l=[1000,10000,100000,1000000]

def simRoulette(game,l):
    for numSpins in l:
        playRoulette(game,numSpins)

#simRoulette(FairRoulette(),l)





