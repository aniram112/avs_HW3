import sys
import string
import datetime
from extender import *

#----------------------------------------------
if __name__ == '__main__':

    if sys.argv[1] == "-f":
        if len(sys.argv) == 5:
            inputFileName  = sys.argv[2]
            outputFileName = sys.argv[3]
            outputFileName2 = sys.argv[4]
        elif len(sys.argv) == 3:
            inputFileName  = sys.argv[2]
            outputFileName = "output.txt"
            outputFileName2 = "outputdelete.txt"
        elif len(sys.argv) == 1:
            print("Incorrect command line! You must write: python main <inputFileName> [<outputFileName> <outputFileName2>]")
            exit()

        timestart = datetime.datetime.now()
        # Чтение исходного файла, содержащего данные, разделенные пробелами и переводами строки
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()

        # Формирование массива строк, содержащего чистые данные в виде массива строк символов.
        strArray = str.split("\n")
        print('==> Start')
        container = Container()
        #figNum = ReadRandom(container,10)
        figNum = ReadStrArray(container, strArray)
        container.Print()

        ofile = open(outputFileName, 'w')
        container.Write(ofile)
        ofile.close()

        container.DeleteLess()
        container.Print()
        ofile = open(outputFileName2, 'w')
        container.Write(ofile)
        ofile.close()
        print('==> Finish')
        print((datetime.datetime.now()-timestart))

    elif sys.argv[1] == "-n":
        count = 0
        if len(sys.argv) == 5:
            count = int(sys.argv[2])
            outputFileName = sys.argv[3]
            outputFileName2 = sys.argv[4]

        elif len(sys.argv) == 3:
            count = int(sys.argv[2])
            outputFileName = "output.txt"
            outputFileName2 = "outputdelete.txt"

        timest = datetime.datetime.now()
        container = Container()
        figNum = ReadRandom(container,count)
        #figNum = ReadStrArray(container, strArray)
        container.Print()

        ofile = open(outputFileName, 'w')
        container.Write(ofile)
        ofile.close()

        container.DeleteLess()
        container.Print()
        ofile = open(outputFileName2, 'w')
        container.Write(ofile)
        ofile.close()
        print('==> Finish')
        print((datetime.datetime.now()-timest))

