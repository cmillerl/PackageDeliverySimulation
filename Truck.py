class Truck:

    MAX_DISTANCE_MILES = 140
    AVG_SPEED = 18
    MAX_PACKAGES = 16
    LOCATION = ["At distribution center", "En route", "Returning"]
    STATUS = ["Waiting for driver or packages", "Delivering packages", "Done for the day"]

    def __init__(self, packagesInTruck, startTime, truckNumber):   
        self.location = self.LOCATION[0]
        self.maxMiles = self.MAX_DISTANCE_MILES
        self.maxPackages = self.MAX_PACKAGES
        self.packagesDelivered = 0
        self.packagesInTruck = packagesInTruck
        self.startTime = startTime
        self.totalMiles = 0
        self.truckNumber = truckNumber
        self.truckStatus = self.STATUS[0]

    def __str__(self):
        return(f"Truck Number: {self.truckNumber}\n"
                f"Packages in Truck: {self.packagesInTruck}\n" 
                f"Current Location: {self.location}\n"
                f"Start Time: {self.startTime}")