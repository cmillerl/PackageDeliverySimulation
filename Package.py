from HashTable import *

hTable = HashTable()

class Package:

    def __init__(self, ID, address, city, state, zipCode, deliveryDeadline, weightKilos, specialNotes, status):
        
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipCode
        self.deliveryDeadline = deliveryDeadline
        self.weightKilos = weightKilos
        self.specialNotes = specialNotes
        self.status = status

    def packageStatus():
            
        try:
            testID = int(input("Enter a package ID to track its status: "))
            packageExists = hTable.lookUp(testID)

            if packageExists:
             print("Package is currently: " + Package.status)
            else:
             print("Package with ID: " + testID + " not found.")
        except ValueError:
            print("Invalid package ID entered.")
            #packageStatus()