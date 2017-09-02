class Program():

    def doSearchUnsorted(arrayData, searchValue):
        #arrayData = []
        for value in arrayData:
            if value == searchValue:
                return 1
        return -1



    def Main():
        arrayData = [2, 8, 15, -2, 31, 4, 1]
        print("doSearchUnsorted(5) = {}".format(Program.doSearchUnsorted(arrayData,5)))
        print("doSearchUnsorted(31) = {}".format(Program.doSearchUnsorted(arrayData, 31)))


if __name__ == "__main__":
    Program.Main()