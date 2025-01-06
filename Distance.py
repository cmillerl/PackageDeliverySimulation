from ImportCSV import *
from Truck import *
from Package import *

import_csv = ImportCSV()

class Distance:
    def __init__(self):
        self.addressTable = address_Table
        self.distanceTable = distance_Table
        self.startAddress =  "4001 South 700 East" #WGU HUB
        self.onTimePackages = 0
        self.offTimePackages = 0
        self.deadlinePackages = 0

    #Removes unnecessary characters from the address.
    #O(1)
    def cleanAddress(self, address):
        return address.replace('\n', ' ').split('(')[0].strip()

    #Returns the distance between two addresses.
    #O(N)
    def getDistance(self, addressOne, addressTwo):
        try:
            addressOne = self.cleanAddress(addressOne)
            addressTwo = self.cleanAddress(addressTwo)
            indexOne = self.addressTable.index(addressOne)
            indexTwo = self.addressTable.index(addressTwo)

            try:
                return float(self.distanceTable[indexOne][indexTwo])
            except IndexError:
                return float(self.distanceTable[indexTwo][indexOne])
            
        except (ValueError, IndexError) as e:
            print(f"Error finding the distance between {addressOne} and {addressTwo} (Distance.getDistance())")
            return float('inf')

    #Part of the greedy algorithm to find the nearest package.
    #O(N)
    def findNearest(self, currentAddress, undeliveredPackages):
        if not undeliveredPackages:
            return None
        
        return min(undeliveredPackages, key = lambda package: self.getDistance(currentAddress, package.address))

    #Part of the greedy algorithm to find the optimal route.
    #O(N^2)
    def optimalRoute(self, truck):
        undelivered = truck.packagesInTruck.copy()
        undeliveredTwo = len(undelivered.copy())
        route = [self.startAddress]
        currentAddress = self.startAddress
        totalDistanceMiles = 0
        currentTime = truck.startTime

        #While there are undelivered packages, find the nearest undelivered package and drive to that location.
        while undelivered:
            nearestLocation = self.findNearest(currentAddress, undelivered)

            if nearestLocation:
                distance = self.getDistance(currentAddress, nearestLocation.address)
                travelTime = timedelta(hours = distance / truck.AVG_SPEED)
                deliveryTime = currentTime + travelTime
                currentTime = deliveryTime
                totalDistanceMiles += distance
                truck.packagesDelivered += 1
                route.append(nearestLocation.address)
                currentAddress = nearestLocation.address
                nearestLocation.deliveryTime = deliveryTime
                nearestLocation.status = "Delivered"
                self.deliveredTime = currentTime
                undelivered.remove(nearestLocation)
                
            if nearestLocation.deliveryDeadline != "EOD":
                self.deadlinePackages += 1
                try:
                    deliveryDeadline = datetime.strptime(nearestLocation.deliveryDeadline, "%I:%M %p")
                    deadlineTime = deliveryDeadline.time()

                    if deliveryTime.time() <= deadlineTime:
                        self.onTimePackages += 1
                    else:
                        self.offTimePackages += 1
                except ValueError:
                    print(f"Error calculating delivery time for package {nearestLocation.ID} (Distance.optimalRoute())")

        #Return to the hub and add the distance to the total miles.
        distanceToHub = self.getDistance(currentAddress, self.startAddress)
        returnTime = timedelta(hours = distanceToHub / truck.AVG_SPEED)
        totalDistanceMiles += distanceToHub
        currentTime += returnTime
        route.append(self.startAddress)

        truck.totalMiles = totalDistanceMiles
        truck.returnTime = currentTime
        truck.route = route
        print(f"Packackages Delivered: {undeliveredTwo}")
        
        #Prints the amount of packages delivered on time, missed deadlines, the route, total miles, and return time.
        if self.deadlinePackages > 0:
            print(f"Total Deadline Packages: {self.deadlinePackages}")
            print(f"Packages delivered by deadline: {self.onTimePackages}")
            print(f"Packages missed delivery deadline: {self.offTimePackages}")

        print(f"Route: {route}")
        print(f"Total Miles: {totalDistanceMiles:.2f}")
        print(f"Return Time: {currentTime.strftime('%I:%M:%S %p')}")

    #Prints the address table.
    #O(N)
    def printAddressTable(self):
        print("All Delivery Addresses")
        print("----------------------")
        for index, address in enumerate(self.addressTable):
            print(f"{index + 1}. {address}")