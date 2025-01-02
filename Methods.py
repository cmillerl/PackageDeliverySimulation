from HashTable import *
from ImportCSV import *
from Truck import *
from Distance import *

import_csv = ImportCSV()

class Methods():
    def __init__(self):
        self.distance_class = Distance()
        self.trucks = []

    def printSortedPackageTable(self):
        print("Package Data Results")
        print("____________________\n")

        allPackages = []

        for bucket in hash_table.table:
            if bucket != None:
                for key, package in bucket:
                    try:
                        int(package.ID)
                        allPackages.append(package)
                    except ValueError:
                        pass
        
        sortedPackages = sorted(allPackages, key = lambda package: int(package.ID))

        for package in sortedPackages:
            print(package)

    def loadAllData(self):
        #Load package data.
        import_csv.fillPackageData()

        #Load distance data.
        import_csv.fillDistanceData()

        #Load address data.
        import_csv.fillAddressData()

    def loadAllTrucks(self):
        truckOne = Truck([], "8:00:00 AM", "Truck One", "4001 South 700 East")
        truckTwo = Truck([], "9:05:00 AM", "Truck Two", "4001 South 700 East")
        truckThree = Truck([], "10:00::00 AM", "Truck Three", "4001 South 700 East")

        truckOne.packagesInTruck = [hash_table.lookUp(str(id)) for id in [1,12,13,14,15,16,17,19,20,21,28,29,33,34,40]]
        truckTwo.packagesInTruck = [hash_table.lookUp(str(id)) for id in [3,6,11,18,22,23,24,25,26,31,32,36]]
        truckThree.packagesInTruck = [hash_table.lookUp(str(id)) for id in [2,4,5,7,8,9,10,27,30,35,37,38,39]]

        self.trucks = [truckOne, truckTwo, truckThree]

    def startDay(self):
        if not self.trucks:
            print("Trucks not loaded.")
            return False
        
        totalMiles = 0
        for truck in self.trucks:
            route, miles = self.distance_class.optimalRoute(truck)
            totalMiles += miles

            print(f"Truck Number: {truck.truckNumber}")
            print(f"Start Time: {truck.startTime}")
            print(f"Route: {'-> '.join(route)}")
            print(f"Total Miles: {miles:.2f}")
            print(f"Packages Delivered: {truck.packagesDelivered}")
            print("-" * 20)
            print(f"Total Miles for all trucks: {totalMiles:.2f}")