from ImportCSV import *
from Truck import *

import_csv = ImportCSV()

class Distance:
    def __init__(self):
        self.address_Table = import_csv.fillPackageData()
        self.distance_Table = import_csv.fillDistanceData()
        self.startAddress =  "4001 South 700 East" #WGU HUB

    def getDistance(self, addressOne, addressTwo):
        try:
            indexOne = address_Table.index(addressOne)
            indexTwo = address_Table.index(addressTwo)
            return float(distance_Table[indexOne][indexTwo])
        except ValueError:
            pass

    def findNearest(self, currentAddress, undeliveredPackages):
        validPackages = [package for package in undeliveredPackages if package is not None]

        if not validPackages:
            return None
        
        return min(validPackages, key = lambda package: self.getDistance(currentAddress, package.address))

    def optimalRoute(self, truck):
        undelivered = truck.packagesInTruck.copy()
        route = [self.startAddress]
        currentAddress = self.startAddress
        totalDistanceMiles = 0

        while undelivered:
            nearestLocation = self.findNearest(currentAddress, undelivered)

            distance = self.getDistance(currentAddress, nearestLocation.address)

            totalDistanceMiles += distance
            route.append(nearestLocation.address)

            currentAddress = nearestLocation.address

        distanceToHub = self.getDistance(currentAddress, self.startAddress)
        totalDistanceMiles += distanceToHub
        route.append(self.startAddress)


        truck.totalMiles = totalDistanceMiles
        truck.route = route
        print(f"Route: {route}")
        print(f"Total Miles: {totalDistanceMiles}")