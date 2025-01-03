class Truck:

    MAX_DISTANCE_MILES = 140
    AVG_SPEED = 18
    MAX_PACKAGES = 16
    STATUS = ["At distribution center", "En route", "Returning"]

    def __init__(self, packagesInTruck, startTime, truckNumber, location):   
        self.location = location
        self.maxMiles = self.MAX_DISTANCE_MILES
        self.maxPackages = self.MAX_PACKAGES
        self.packagesDelivered = 0
        self.packagesInTruck = packagesInTruck
        self.startTime = startTime
        self.totalMiles = 0
        self.truckNumber = truckNumber
        self.truckStatus = self.STATUS[0]

    def __str__(self):
        try:
            packageIDs = [str(package.ID) for package in self.packagesInTruck]
            packageList = ', '.join(packageIDs) if packageIDs else "No packages in truck."
            return(f"Truck Number: {self.truckNumber}\n"
                    f"Packages in Truck: {packageList}\n" 
                    f"Current Location: {self.location}\n"
                    f"Start Time: {self.startTime}")
        except AttributeError:
            return "Error printing truck information. (Truck.__str__())"