from HashTable import *
from ImportCSV import *
from Package import *
from Truck import *
from Methods import *

import_csv = ImportCSV()
method_class = Methods()

class Main():
    def __init__(self):

        #import_csv.fillPackageData()

        #method_class.printSortedPackageTable()

        import_csv.fillDistanceData

        print(import_csv.distanceTable)

Main()
