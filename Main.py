from HashTable import *
from ImportCSV import *
from Package import *
from Truck import *
from Distance import *\

class Main:
    def __init__(self):
        truckOne = Truck(driver = Truck.DRIVERS[0], location = Truck.LOCATIONS[0], truckNumber = 1)
        truckTwo = Truck(driver = Truck.DRIVERS[1], location = Truck.LOCATIONS[0], truckNumber = 2)
        truckThree = Truck(driver = Truck.DRIVERS[2], location = Truck.LOCATIONS[0], truckNumber = 3)
        print(truckOne)

Main()