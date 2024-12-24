import csv
from HashTable import *
from Distance import *

hTable = HashTable()
dTable = distanceData

def getPackageData():

    with open("packageDataFile.csv") as packageFile: #Import the package data from a .csv file.
        csvPackage = csv.reader(packageFile)

    for row in csvPackage:
        ID = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zipCode = row[4]
        deliveryDeadline = row[5]
        weightKilos = row[6]
        specialNotes = row[7]
        status = "At distribution center."

        Package = Package(ID, address, city, state, zipCode, deliveryDeadline, weightKilos, specialNotes, status)

        hTable.insertItem(Package)

def getDistanceData():
    
    with open("distanceDataFile.csv") as distanceFile: #Import the distance data from a .csv file.
        csvDistance = csv.reader(distanceFile)
