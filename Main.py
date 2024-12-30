#Student ID: 012217037

from HashTable import *
from ImportCSV import *
from Package import *
from Truck import *
from Methods import *
from Distance import *

import_csv = ImportCSV()
method_class = Methods()
distance_class = Distance()

class Main():
    def __init__(self):

        print("WGUPS Routing Program\n" + 
              "_____________________\n")

        import_csv.fillPackageData()
        #method_class.printSortedPackageTable()
        #Test to make sure data is imported correctly.

        import_csv.fillDistanceData()
        #print(distance_Table)
        #Test to make sure data is imported correctly.

        import_csv.fillAddressData()
        #print(address_Table)
        #Test to make sure data is imported correctly.

        truckOne = Truck([1,12,13,14,15,16,17,19,20,21,28,29,33,34,40], None, "Truck One", startAddress)
        truckTwo = Truck([3,6,11,18,22,23,24,25,26,31,32,36], None, "Truck Two", startAddress)
        truckThree = Truck([2,4,5,7,8,9,10,27,30,35,37,38,39], None, "Truck Three", startAddress)

        print(truckOne)

Main()
