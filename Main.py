#Student ID: 012217037

from HashTable import *
from ImportCSV import *
from Package import *
from Truck import *
from Methods import *
from Distance import *

method_class = Methods()
distance_class = Distance()

class Main():
    def __init__(self):

        try:

            print("WGUPS Routing Program\n" + 
                  "_____________________\n")
            
            method_class.loadAllData()

            distance_class.printAddressTable()

        except ValueError:
            print("Error initializing program")
Main()
