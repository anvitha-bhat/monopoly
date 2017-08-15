class Player:
    def __init__(self,money,pos):
      self._money = money
      self._pos = pos

    def getmoney(self):
        return self._money

    def move(self,val):
        self._pos = (self._pos + val) % 40

    def getpos(self):
        return self._pos

    def givemoney(self,val):
        self._money = self._money-val

    def takemoney(self,val):
        self._money = self._money+val

    def __str__(self):
        return 'gamer : { money : ' + str(self._money) + ' }'


if __name__ == '__main__':
    a = Player()
    print a.getmoney()
    a.takemoney(10)
    print a.getmoney()
    a.givemoney(5)
    print a
