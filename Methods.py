from HashTable import *
from ImportCSV import *
from Truck import *
from Distance import *
from Package import *

import_csv = ImportCSV()

class Methods():
    def __init__(self):
        self.distance_class = Distance()
        self.trucks = []
        self.total_miles = 0

    #Sorts the package table in order of ID from least to greatest and prints the results.
    #O(n log n)
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
        #O(N)
        import_csv.fillPackageData()

        #Load distance data.
        #O(N)
        import_csv.fillDistanceData()

        #Load address data.
        #O(N)
        import_csv.fillAddressData()


    #Load trucks one, two, and three with the respective data.
    #O(N)
    def loadAllTrucks(self):
        truckOne = Truck([], "8:00:00 AM", "Truck One", "4001 South 700 East")
        truckTwo = Truck([], "9:05:00 AM", "Truck Two", "4001 South 700 East")
        truckThree = Truck([], "10:20:00 AM", "Truck Three", "4001 South 700 East")
    
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
                    package.truckNumber = truck.truckNumber
    
        self.trucks = [truckOne, truckTwo, truckThree]
        return self.trucks
    
    #Starts the delivery process for all trucks beginning at 8:00:00 AM.
    #O(N^2)
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
                print(f"All packages delivered in {self.total_miles:.2f} miles.\n")
            else:  
                print(f"Not all packages delivered under the 140 mile limit instead {self.total_miles:.2f} miles taken.\n")

            return True
        except ValueError:
            print("Error starting deliveries. (Methods.startDeliveries())")
            return False
        
    #Prints trucks, useful for debugging.
    #O(N)    
    def printTrucks(self):
        for index, Truck in enumerate(self.trucks, 1):
            print(f"Truck {index} Details\n")
            print("-----------------")
            print(Truck)
            print("\n")

    #Look up a package by ID number.
    #O(1)
    def lookupPackage(self):
        try:
            packageID = int(input("Enter the package ID you want to look up (1-40): "))
            package = hash_table.lookUp(str(packageID))

            if package:
                print(package)
            else:
                print(f"Package {packageID} not found.")

        except ValueError:
            print("Invalid input. Exiting program. Methods.lookupPackage()")
            exit()

    #Main menu for user interaction.
    def menu(self):
        print("Welcome to the WGUPS Routing Program.")
        print("-------------------------------------")
        print("Select an option from the menu below (1-5)")
        print("1. Check all packages status by time.")
        print("2. Look up a package by ID number (1-40).")
        print("3. Print packages sorted by ID number.")
        print("4. Print truck details.")
        print("5. Exit the program.")
            
        try:
            choice = int(input("\nEnter a valid number (1-5): "))

            if choice == 1:
                print("\n")
                self.checkPackageStatusAtTime()
            elif choice == 2:
                print("\n")
                self.lookupPackage()
            elif choice == 3:
                print("\n")
                self.printSortedPackageTable()
            elif choice == 4:
                print("\n")
                self.printTrucks()
            elif choice == 5:
                print("\nExiting program.\n")
                exit()
            else:
                print("\nInvalid input.\n")
                self.menu()

        except ValueError:
            print("\nInvalid input.\n")
            self.menu()

    #Checks packages status at a certain time.
    #O(N)
    def checkPackageStatusAtTime(self):
        try:
            time = input("Enter a time to check the status of all packages. (HH:MM:SS AM/PM): ")
            timeFormat = datetime.strptime(time, "%I:%M:%S %p")

            print(f"\nPackage Status at {timeFormat.strftime('%I:%M:%S %p')}")
            print("____________________________________________________\n")

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
                for truck in self.trucks:
                    if package in truck.packagesInTruck:
                        if timeFormat < truck.startTime:
                            status = "at the hub"
                            print(f"Package {package.ID}, {package.weightKilos}kg, on {truck.truckNumber.lower()} is at the hub (4001 South 700 East, Salt Lake City, UT, 84107) at {timeFormat.strftime('%I:%M:%S %p')}. Package {package.ID} will be delivered to {package.address}, {package.city}, {package.state}, {package.zipCode} and the delivery deadline is {package.deliveryDeadline}.")
                        elif not package.deliveryTime or timeFormat < package.deliveryTime:
                            status = "en route"
                            print(f"Package {package.ID}, {package.weightKilos}kg, on {truck.truckNumber.lower()} is {status} to {package.address}, {package.city}, {package.state}, {package.zipCode} at {timeFormat.strftime('%I:%M:%S %p')}. The package delivery deadline is {package.deliveryDeadline}.")
                        else:
                            status = "delivered"
                            print(f"Package {package.ID}, {package.weightKilos}kg, on {truck.truckNumber.lower()} was delivered to {package.address}, {package.city}, {package.state}, {package.zipCode} at {package.deliveryTime.strftime('%I:%M:%S %p')}. The package delivery deadline was {package.deliveryDeadline}.")
            
            print("\nTruck Mileage")
            print("_____________\n")
            combinedMiles = 0
            for truck in self.trucks:
                    milesTraveled = 0
                    for deliveryTime, miles in truck.miles:
                        if timeFormat >= deliveryTime:
                            milesTraveled = miles
                    print(f"{truck.truckNumber} has traveled {milesTraveled:.2f} miles at {timeFormat.strftime('%I:%M:%S %p')}.")
                    combinedMiles += milesTraveled
            print(f"The combined mileage of all trucks at {timeFormat.strftime('%I:%M:%S %p')} is {combinedMiles:.2f} miles.\n")

        except ValueError:
            print("Invalid input. Exiting program. Methods.checkPackageStatusAtTime()")