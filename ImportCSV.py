import csv
from HashTable import *
from Package import *

ht = HashTable()
    
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

        ht.insertItem(newPackage.ID, newPackage)

print("Hash Table test: ")
for bucket in ht.table:
    if bucket is not None:
        for key, package in bucket:
            print(package)