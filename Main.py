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
        import_csv.fillDistanceData()

        truckOne = Truck([], "8:00:00 AM", "Truck One", "4001 South 700 East")
        truckTwo = Truck([], "9:05:00 AM", "Truck Two", "4001 South 700 East")
        truckThree = Truck([], "10:00::00 AM", "Truck Three", "4001 South 700 East")

        truckOne.packagesInTruck = [hash_table.lookUp(str(id)) for id in [1,12,13,14,15,16,17,19,20,21,28,29,33,34,40]]
        truckTwo.packagesInTruck = [hash_table.lookUp(str(id)) for id in [3,6,11,18,22,23,24,25,26,31,32,36]]
        truckThree.packagesInTruck = [hash_table.lookUp(str(id)) for id in [2,4,5,7,8,9,10,27,30,35,37,38,39]]

        for truck in [truckOne, truckTwo, truckThree]:
            optimalRoute, totalMiles = distance_class.optimalRoute(truck)
            print(f"Truck Number: {self.truckNumber}")
            print(f"Route: {'-> '.join(optimalRoute)}")
            print(f"Total Miles: {totalMiles:.2f}")
            print(f"Packages Delivered: {truck.packagesDelivered}")

Main()
