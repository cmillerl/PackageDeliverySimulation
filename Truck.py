class Truck:

    maxDistance = 140
    maxSpeed = 18
    maxPackages = 16

    def __init__(self, currentDriver, location, packagesDelivered, packagesInTruck, truckStatus, totalMiles):
        
        self.currentDriver = currentDriver
        self.location = location
        self.packagesDelivered = packagesDelivered
        self.packagesInTruck = packagesInTruck
        self.truckStatus = truckStatus
        self.totalMiles = totalMiles