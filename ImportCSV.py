import csv
from HashTable import *
from Package import *

hash_table = HashTable()
distance_Table = []
address_Table = []

class ImportCSV():
    def __init__(self):
        pass

    #Fills the hash table with package data.
    #O(N)
    def fillPackageData(self):
        with open('csvFiles\packageData.csv', 'r') as packageData:
            csv_reader = csv.reader(packageData, delimiter = ',')
            
            try:
                for row in csv_reader:
                    ID = row[0].strip().replace('ï»¿', '')
                    address = row[1]
                    city = row[2]
                    state = row[3]
                    zipCode = row[4]
                    deliveryDeadline = row[5]
                    weightKilos = row[6]
                    specialNotes = row[7]
                    status = "At WGU Hub."

                    newPackage = Package(ID, address, city, state, zipCode, deliveryDeadline, weightKilos, specialNotes, status)
                    hash_table.insertItem(ID, newPackage)
                    #print(f"Package {ID} added to the hash table.") for debugging purposes.
            except ValueError:
                print("Error loading package data. (ImportCSV.fillPackageData())")

    #Fills the distance table with distance data.
    #O(N)
    def fillDistanceData(self):
        global distance_Table
        with open('csvFiles\distanceData.csv', 'r') as distanceData:
            csv_reader = csv.reader(distanceData, delimiter = ',')

            try:
                for row in csv_reader:
                    cleanedRow = [cell.strip() for cell in row if cell.strip()]
                    if cleanedRow:
                        distance_Table.append(cleanedRow)
            except ValueError:
                print("Error loading distance data. (ImportCSV.fillDistanceData())")
            
    #Fills the address table with address data.
    #O(N)
    def fillAddressData(self):
        global address_Table
        with open('csvFiles/addressData.csv', 'r') as addressData:
            csv_reader = csv.reader(addressData, delimiter = ',')

            try:
                for row in csv_reader:
                    if row:
                        address = row[1].strip()
                        address_Table.append(address)
            except ValueError:
                print("Error loading address data. (ImportCSV.fillAddressData())")