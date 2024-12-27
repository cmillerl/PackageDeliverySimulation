import csv
from HashTable import *
from Package import *

hash_table = HashTable()

class ImportCSV():
    def __init__(self):
        self.distanceTable = []

    def fillPackageData(self):
        with open('csvFiles\packageData.csv', 'r') as packageData:
            csv_reader = csv.reader(packageData, delimiter = ',')
            for row in csv_reader:
                ID = row[0]
                address = row[1]
                city = row[2]
                state = row[3]
                zipCode = row[4]
                deliveryDeadline = row[5]
                weightKilos = row[6]
                specialNotes = row[7]
                status = "At distribution center."

                newPackage = Package(ID, address, city, state, zipCode, deliveryDeadline, weightKilos, specialNotes, status)
                
                hash_table.insertItem(newPackage.ID, newPackage)

    def fillDistanceData(self):
        with open('csvFiles\distanceData.csv', 'r') as distanceData:
            csv_reader = csv.reader(distanceData, delimiter = ',')
            for row in csv_reader:
                ImportCSV.distanceTable.append(row)
            for i in range(len(ImportCSV.distanceTable)):
                for j in range(len(ImportCSV.distanceTable)):
                    ImportCSV.distanceTable[i][j] = ImportCSV.distanceTable[j][i]