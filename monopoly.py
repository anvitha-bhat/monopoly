import gamer
import random

class Monopoly:
    _playerlist = []

    def __init__(self,number):
        self._playerscount = number
        self._playerturn = 0
        for i in range(number):
            newplayer =  gamer.Player(100,0)
            self._playerlist.append(newplayer)

    def rolldice(self):
        diceval = random.randint(1,6)
        self._playerlist[self._playerturn].move(diceval)
        self._playerturn = (self._playerturn+1)%self._playerscount

    # def display(self):
    #     for i in range(len(self._playerlist)):
    #         print '{ '+str(self._playerlist[i])+' '+str(self._playerlist[i].getpos())+' }'
    def display(self):
        for player in self._playerlist:
            print '{'+str(player)+' '+str(player.getpos())+'}'

a = Monopoly(4)
for i in range(1,50):
    a.rolldice()
    a.display()
    print ''
