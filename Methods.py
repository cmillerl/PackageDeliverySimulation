from HashTable import *
from ImportCSV import *
from Truck import *
from Distance import *

import_csv = ImportCSV()

class Methods():
    def __init__(self):
        self.distance_class = Distance()
        self.trucks = []
        self.total_miles = 0

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
        truckThree = Truck([], "10:00:00 AM", "Truck Three", "4001 South 700 East")
    
        package_lists = {
            truckOne: [13,14,15,16,19,20,1,21,29,30,31,34,37],
            truckTwo: [3,6,18,25,26,28,32,36,38,40],
            truckThree: [2,4,5,7,8,9,10,11,12,17,22,23,24,27,33,35,39]}
    
        for truck, package_ids in package_lists.items():
            truck.packagesInTruck = []
            for pid in package_ids:
                package = hash_table.lookUp(str(pid))
                if package:
                    truck.packagesInTruck.append(package)
    
        self.trucks = [truckOne, truckTwo, truckThree]
        return self.trucks
    
    def startDeliveries(self):
        try:
            for truck in self.trucks:
                print(f"\nCalculating route for {truck.truckNumber}")
                self.distance_class.optimalRoute(truck)
                self.total_miles += truck.totalMiles
                
            print("\nDelivery Summary")
            print("-" * 20)
            print(f"Total Miles Traveled: {self.total_miles:.1f}")
            print(f"Total Packages Delivered: {sum(truck.packagesDelivered for truck in self.trucks)}")
            
            return True
        except ValueError:
            print("Error starting deliveries.")
            return False