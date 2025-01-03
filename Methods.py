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
            truckTwo: [3,6,18,25,26,28,32,36,38,39,40],
            truckThree: [2,4,5,7,8,9,10,11,12,17,22,23,24,27,33,35]}
    
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
            firstTime = datetime.strptime("8:00:00 AM", "%I:%M:%S %p")

            for truck in self.trucks:
                print("\n" + truck.truckNumber)
                print("----------")
                print(f"Depature Time: {truck.startTime.strftime('%I:%M:%S %p')}")
                self.distance_class.optimalRoute(truck)
                self.total_miles += truck.totalMiles

            lastTime = max(truck.returnTime for truck in self.trucks)
            totalTime = lastTime - firstTime
            hours = int(totalTime.total_seconds() // 3600)
            minutes = int((totalTime.total_seconds() % 3600) // 60)
            seconds = int(totalTime.total_seconds() % 60)

                
            print("\nDelivery Day Summary")
            print("--------------------")
            print(f"Total Packages Delivered: {sum(truck.packagesDelivered for truck in self.trucks)} out of 40.")
            print(f"Total Time Taken: {hours} hours {minutes} minutes {seconds} seconds.")

            if self.distance_class.onTimePackages == self.distance_class.deadlinePackages:
                print("All packages delivered on time.")
            else:
                print(f"{self.distance_class.offTimePackages} packages delivered late.")

            if self.total_miles <= 140:
                print(f"All packages delivered in {self.total_miles:.2f} miles.")
            else:  
                print(f"Not all packages delivered under the 140 mile limit instead {self.total_miles:.2f} miles taken.")

            return True
        except ValueError:
            print("Error starting deliveries. (Methods.startDeliveries())")
            return False
        
    def printTrucks(self):
        for index, Truck in enumerate(self.trucks, 1):
            print(f"Truck {index} Details\n")
            print("-----------------")
            print(Truck)
            print("\n")