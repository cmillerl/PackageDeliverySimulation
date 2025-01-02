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
            
            try:
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
            except ValueError:
                print("Error loading package data.")

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
                print("Error loading distance data.")
            
    def fillAddressData(self):
        global address_Table
        with open('csvFiles/addressData.csv', 'r') as addressData:
            csv_reader = csv.reader(addressData, delimiter = ',')

            try:
                for row in csv_reader:
                    if row:
                        address = row[1].strip()
                        address_Table.append(address)
            except Exception as e:
                print(f"Error in fillAddressData: {e}")