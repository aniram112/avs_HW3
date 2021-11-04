import random
import string
from cypher import *


# ----------------------------------------------
# циклический шифр
class Cyclic(Cypher):
    def __init__(self):
        self.cypher = 0
        self.cyphered = ""
        self.decyphered = ""


    def ReadStrArray(self, strArray, i):
        if i >= len(strArray) - 1:
            return 0
        self.cyphered = strArray[i]
        self.cypher = int(strArray[i + 1])
        #self.decyphered = self.cyphered
        for item in self.cyphered:
            self.decyphered += chr((self.cypher + ord(item)))
        return i+2

    def ReadRand(self):
        self.cypher = random.randint(1,10)
        length = random.randint(2,15)
        for i in range(0, length):
            symb = random.choice(string.ascii_lowercase)
            self.cyphered += symb
            self.decyphered += chr((self.cypher + ord(symb)))
        pass


    def Print(self):
        print("cyclic cypher: cyphered text = ", self.cyphered, ", decyphered text = ", self.decyphered,
              ". function result = ", round(self.Func(),2))
        pass


    def Write(self, ostream):
        ostream.write("cyclic cypher: cyphered text = {} , decyphered text = {}. function result = {}".format \
                          (self.cyphered, self.decyphered, round(self.Func(),2)))
        pass


    def Func(self):
        sum = 0.0
        for x in self.decyphered:
            sum += ord(x)
        return sum / len(self.decyphered)
