from ImportCSV import *
from Truck import *

import_csv = ImportCSV()

class Distance:
    def __init__(self):
        self.addressTable = address_Table
        self.distanceTable = distance_Table
        self.startAddress =  "4001 South 700 East" #WGU HUB

    def cleanAddress(self, address):
        return address.replace('\n', ' ').split('(')[0].strip()

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
            print(f"Error finding the distance between {addressOne} and {addressTwo}")
            return float('inf')

    #Part of the greedy algorithm to find the nearest package.
    def findNearest(self, currentAddress, undeliveredPackages):
        validPackages = [package for package in undeliveredPackages if package is not None]

        if not validPackages:
            return None
        
        return min(validPackages, key = lambda package: self.getDistance(currentAddress, package.address))

    #Part of the greedy algorithm to find the optimal route.
    def optimalRoute(self, truck):
        undelivered = truck.packagesInTruck.copy()
        route = [self.startAddress]
        currentAddress = self.startAddress
        totalDistanceMiles = 0

        #While there are undelivered packages, find the nearest undelivered package and drive to that location.
        while undelivered:
            nearestLocation = self.findNearest(currentAddress, undelivered)

            if nearestLocation:
                distance = self.getDistance(currentAddress, nearestLocation.address)
                totalDistanceMiles += distance
                truck.packagesDelivered += 1
                route.append(nearestLocation.address)
                currentAddress = nearestLocation.address
                undelivered.remove(nearestLocation)

        #Return to the hub and add the distance to the total miles.
        distanceToHub = self.getDistance(currentAddress, self.startAddress)
        totalDistanceMiles += distanceToHub
        route.append(self.startAddress)

        truck.totalMiles = totalDistanceMiles
        truck.route = route
        print(f"Route: {route}")
        print(f"Total Miles: {totalDistanceMiles}")

    def printAddressTable(self):
        print("\nAll Delivery Addresses:")
        print("----------------------")
        for index, address in enumerate(self.addressTable):
            print(f"{index + 1}. {address}")