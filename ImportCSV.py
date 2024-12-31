import csv
from HashTable import *
from Package import *

hash_table = HashTable()
distance_Table = []
address_Table = []

class ImportCSV():
    def __init__(self):
        pass

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
        global distance_Table

        with open('csvFiles\distanceData.csv', 'r') as distanceData:
            csv_reader = csv.reader(distanceData, delimiter = ',')
            distance_Table = list(csv_reader)

            try:
                for i in range(len(distance_Table)):
                    for j in range(len(distance_Table[i])):
                        if distance_Table[i][j]:
                           distance_Table[i][j] = float(distance_Table[i][j])
            except ValueError:
                pass
            
            try:
                for i in range(len(distance_Table)):
                    for j in range(i + 1, len(distance_Table)):
                        if distance_Table[i][j] and not distance_Table [j][i]:
                            distance_Table[j][i] = distance_Table [i][j]
            except ValueError:
                pass

    def fillAddressData(self):
        global address_Table

        with open('csvFiles/distanceData.csv', 'r') as addressData:
            csv_reader = csv.reader(addressData, delimiter = ',')
            for row in csv_reader:
                try:
                    if address_Table[0] != "":
                        address_Table.append(row[0])
                except ValueError:
                    pass