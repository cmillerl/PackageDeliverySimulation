import csv
from HashTable import *

#with open(#Input file path) as packageFile:
    #csv_reader = csv.reader(packageFile)

HashTable = HashTable()

def getPackageData():

    for Package in csv_reader:
        ID = Package[0]
        address = Package[1]
        city = Package[2]
        state = Package[3]
        zipCode = Package[4]
        deliveryDeadline = Package[5]
        weightKilos = Package[6]
        specialNotes = Package[7]
        status = "At distribution center."

        Package = Package(ID, address, city, state, zipCode, deliveryDeadline, weightKilos, specialNotes, status)

        HashTable.insertItem(Package)