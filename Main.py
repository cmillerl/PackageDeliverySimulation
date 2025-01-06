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
            #Load all data into the correct arrays.
            #O(N)
            method_class.loadAllData()
            print("Data loaded successfully.\n")

            #Load all trucks with packages.
            #O(N)
            method_class.loadAllTrucks()
            print("Trucks loaded successfully.")

            #Start delivery process.
            #O(N^2)
            method_class.startDeliveries()

            #Main menu for user interaction.
            method_class.menu()

        except ValueError:
            print("Error initializing program (Main.__init__())")

Main()
