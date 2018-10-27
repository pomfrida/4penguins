import random

class makeMove(object):

    def __init__(self, mypos, mydir, myhp, myrange, mydamage):
        self.number = 1
        self.mypos = mypos
        self.mydir = mydir
        self.myhp = myhp
        self.myrange = myrange
        self.mydamage = mydamage

    def indanger(self,dist,enemyrange):
        if dist < enemyrange:
            margin = dist-enemyrange
            return 'danger', margin
        else:
            return 'safe', None


    # Check for nearby objects
    def nearby(self, objects):
        where = []
        dist = []

        for obj in objects:

            if obj[0] - self.mypos[0] < 0 & obj[1] == self.mypos[1]:
                distance = abs(obj[0] - self.mypos[0])
                dist.append(distance)
                where.append('l')
            elif obj[0] - self.mypos[0] > 0 & obj[1] == self.mypos[1]:
                distance = abs(obj[0] - self.mypos[0])
                dist.append(distance)
                where.append('r')

            elif obj[1] - self.mypos[1] < 0 & obj[0] == self.mypos[0]:
                distance = abs(obj[1] - self.mypos[1])
                dist.append(distance)
                where.append('f')

            elif obj[1] - self.mypos[1] > 0 & obj[0] == self.mypos[0]:
                distance = abs(obj[1] - self.mypos[1])
                dist.append(distance)
                where.append('b')

        return where, dist

    # Who has the most hp?
    def superiorhp(self,enemyhp):
        if self.myhp > enemyhp:
            return 'me'
        else:
            return 'enemy'

    # Who has the most range?
    def superiorrange(self,enemyrange):
        if self.myrange > enemyrange:
            return 'me'
        else:
            return 'enemy'

    # Who has the moset damage?
    def superiordamage(self,enemydamage):
        if self.mydamage > enemydamage:
            return 'me'
        else:
            return 'enemy'

    # Some set functions...
    def setpos(self, mypos):
        self.mypos = mypos

    def sethp(self, hp):
        self.hp = hp

    def setdamage(self, damage):
        self.damage = damage

    def setrange(self, range):
        self.range = range

    # The function that decides the move..
    def doSomething(self,enemydata,bonusdata,walls,fire):
        moves = ['rotate-left', 'rotate-right', 'advance', 'return', 'shoot', 'pass']

        ##
        #walls = []

        #isnear          = False

        #if len(enemydata) == 1:
        #    enemyhp     = enemydata
        #else:
        #    enemypos    = enemydata[0,1]
        #    enemyhp     = enemydata[2]
        #    enemydir    = enemydata[3]
        #    enemyammo   = enemydata[4] #cant see how it should be useful?
        #    enemyrange  = enemydata[5]
        #    enemydamage = enemydata[6]
        #    isnear      = True

        #cont = True
        #todo = []

        #where, distance = self.nearby(enemypos) # only returns one

        #if where == 'r' and self.mydir == 'left' or where == 'l' and self.mydir == 'right':
        #    status, margin = self.indanger(distance, enemyrange)
        #    if status == 'danger':
        #        todo = [2,3]
        #    else:
        #        todo = [1,2,3,4]

        #elif where == 'f' and self.mydir == 'bottom' or where == 'b' and self.mydir == 'front':
        #    status, margin = self.indanger(distance, enemyrange)
        #    todo = 4
        #    cont = False

        ##if cont == True:
        ##    where, distance = self.isnear(wall)


        rnd = random.randint(0, 5)
        return moves[rnd] #for now... do a random move
