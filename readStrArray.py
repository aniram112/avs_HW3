import random

from extender import *
# ввод из файла
def ReadStrArray(container, strArray):
    arrayLen = len(strArray)
    i = 0
    figNum = 0
    while i < arrayLen:
        str = strArray[i]
        key = int(str)
        if key == 1:
            i += 1
            shape = Symbols()
            i = shape.ReadStrArray(strArray, i)
        elif key == 2:
            i += 1
            shape = Cyclic()
            i = shape.ReadStrArray(strArray, i)
        elif key == 3:
            i += 1
            shape = Numbers()
            i = shape.ReadStrArray(strArray, i)
        else:
            return figNum
        if i == 0:
            return figNum
        figNum += 1
        container.store.append(shape)
    return figNum

# рандомный ввод
def ReadRandom(container, arrayLen):
    figNum = 0
    while figNum < arrayLen:
        #str = strArray[i]
        key = random.randint(1,3)
        if key == 1:
            shape = Symbols()
            shape.ReadRand()
        elif key == 2:
            shape = Cyclic()
            shape.ReadRand()
        elif key == 3:
            shape = Numbers()
            shape.ReadRand()
        else:
            return figNum
        figNum += 1
        container.store.append(shape)
    return figNum
