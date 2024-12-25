class Truck:

    DRIVERS = ["John", "Ethan", "None"]
    MAX_DISTANCE = 140
    MAX_SPEED = 18
    MAX_PACKAGES = 16
    LOCATIONS = ["At distribution center", "En route", "Returning"]
    STATUS = ["Waiting for driver or packages", "Delivering packages", "Done for the day"]

    def __init__(self, driver, location, truckNumber):    
        self.driver = driver
        self.location = location
        self.packagesDelivered = 0
        self.packagesInTruck = []
        self.truckStatus = self.STATUS[0]
        self.totalMiles = 0
        self.truckNumber = truckNumber

    def __str__(self):
        return(f"Truck: {self.truckNumber}\n"
                f"Driver: {self.driver}\n" 
                f"Location: {self.location}")