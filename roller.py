from random import randint as r
from random import random as randFloat

class Roller:
    def __init__(self, size=20):
        self.list = [0]*size
        self.population = 0

    def populate(self, num):
        self.population += num
        for i in range(0,num):
            self.list[ r( 0, len(self.list)-1 ) ] += 1

    def populateAdvantage(self,num):
        self.population += num
        for i in range(0,num):
            x = r( 0, len(self.list)-1 )
            y = r( 0, len(self.list)-1 )

            self.list[ max(x,y) ] += 1

    def poulateWeighted(self,num,weight=2):
        self.population += num
        for i in range(0,num):
            x = round((1 - randFloat()**weight) * (len(self.list)-1))

            self.list[ x ] += 1

    def graph(self):
        for i in range(0,len(self.list)):
            percent = (self.list[i] / self.population) * 100
            intPercent = round(percent)
            print("{0:>2}: {1:>4.1f}% {2}".format(i+1, percent, '|'*intPercent))


def main():
    roller1 = Roller()
    roller2 = Roller()
    roller3 = Roller()

    roller1.populate(1000000)
    roller2.populateAdvantage(1000000)
    roller3.poulateWeighted(1000000)

    print("Rolling 1d20")
    roller1.graph()

    print("\nRolling 1d20 with advantage")
    roller2.graph()

    print("\nRolling a weighted average")
    roller3.graph()

if __name__ == '__main__':
    main()