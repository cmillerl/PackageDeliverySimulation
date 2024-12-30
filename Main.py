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

        import_csv.fillDistanceData()
        #print(distance_Table)

        import_csv.fillAddressData()
        #print(address_Table)

        truckOne = Truck([], None, "Truck One")
        truckTwo = Truck([], None, "Truck Two")
        truckThree = Truck([], None, "Truck Three")

        print(truckOne)

Main()
