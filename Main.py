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
            
            #Load all data into the correct arrays.
            method_class.loadAllData()
            print("Data loaded successfully.\n")

            #Load all trucks with packages.
            method_class.loadAllTrucks()
            print("Trucks loaded successfully.")

            #Start the truck deliveries.
            method_class.startDeliveries()

            

        except ValueError:
            print("Error initializing program (Main.__init__())")
Main()
