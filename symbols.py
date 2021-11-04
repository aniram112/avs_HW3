import random
import string
from cypher import *


# ----------------------------------------------
# шифр замены символами
class Symbols(Cypher):
    def __init__(self):
        self.length = 0
        self.cyphered = ""

        self.decyphered = ""
        self.cypher1 = ""
        self.cypher2 = ""


    def ReadStrArray(self, strArray, i):
        # должно быт как минимум три непрочитанных значения в массиве
        if i >= len(strArray) - 1:
            return 0
        #self.length = strArray[i]

        self.cyphered = strArray[i].replace(" ","")
        strArrSplit = strArray[i+1].split(" ")

        for j in range(0, len(strArrSplit), 2):
            self.cypher1 += strArrSplit[j]
            self.cypher2 += strArrSplit[j+1]

        for j in range(0, len(self.cyphered)):
            for k in range(0, len(self.cypher1)):
                if self.cyphered[j] == self.cypher1[k]:
                    self.decyphered += self.cypher2[k]
        return i+2

    def ReadRand(self):
        self.length = random.randint(3,15)
        for i in range(0, self.length):
            self.cyphered += random.choice(string.ascii_lowercase)
            self.decyphered += random.choice(string.ascii_lowercase)

        self.cypher1 = self.cyphered
        self.cypher2 = self.decyphered
        pass


    def Print(self):
        print("symbols cypher: cyphered text = ", self.cyphered, ", decyphered text = ", self.decyphered,
              ". function result = ", round(self.Func(),2))
        pass


    def Write(self, ostream):
        ostream.write("symbols cypher: cyphered text = {} , decyphered text = {}. function result = {}".format \
                          (self.cyphered, self.decyphered, round(self.Func(),2)))
        pass


    def Func(self):
        sum = 0.0
        for x in self.decyphered:
            sum += ord(x)
        return sum / len(self.decyphered)

