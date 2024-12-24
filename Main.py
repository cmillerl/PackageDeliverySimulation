from HashTable import *
from ImportCSV import *
from Package import *
from Truck import *
from Driver import *
from Distance import *

def packageStatus():
            
    try:
        testID = int(input("Enter a package ID to track its status: "))
        packageExists = HashTable.lookUp(testID)

        if packageExists:
            print("Package is currently: " + Package.status)
        else:
            print("Package with ID: " + testID + " not found.")
    except ValueError:
        print("Invalid package ID entered.")
        packageStatus()

class Main:
    HashTable = HashTable()
    packageStatus()

Main()