#----------------------------------------------
class Container:
    def __init__(self):
        self.store = []

    #def ReadStrArray(self, strArray):

    def Print(self):
        print("Container is store", len(self.store), "cyphers:")
        for shape in self.store:
            shape.Print()

        #self.DeleteLess(mean)
        #print("Mean: ", round(mean,2),"Sum: ",round(sum,2),"Len: ",len(self.store))
        #for shape in self.store:
         #   shape.Print()
        #print("Summa of Perimeters  = ", self.Func())
        pass

    def Write(self, ostream):
        ostream.write("Container is store {} cyphers:\n".format(len(self.store)))
        for shape in self.store:
            shape.Write(ostream)
            ostream.write("\n")
        #ostream.write("Summa of Perimeters  = {}\n".format(self.Func()))
        pass

    def Mean(self):
        sum = 0.0
        for item in self.store:
            sum += item.Func()
        mean = sum/len(self.store)
        return mean

    def DeleteLess(self):
        sum = 0.0
        for item in self.store:
            sum += item.Func()
        mean = sum/len(self.store)

        for item in self.store:
            if item.Func() < mean:
                self.store.remove(item)


