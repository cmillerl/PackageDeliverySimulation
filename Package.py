from datetime import datetime, timedelta

class Package:

    def __init__(self, ID, address, city, state, zipCode, deliveryDeadline, weightKilos, specialNotes, status):
        
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deliveryDeadline = deliveryDeadline
        self.deliveryTime = None
        self.weightKilos = weightKilos
        self.specialNotes = specialNotes
        self.status = status

    def __str__(self):
        return (f"Package ID: {self.ID}\n" 
                f"Delivery Address: {self.address}, {self.city}, {self.state}, {self.zipCode}\n" 
                f"Weight: {self.weightKilos}kg \n" 
                f"Status: {self.status}\n"
                f"Delivery Deadline: {self.deliveryDeadline}\n" 
                f"Notes: {self.specialNotes}\n" 
                f"Delivery Time: {self.deliveryTime.strftime('%I:%M:%S %p')}\n"
                "_____________________________________________________________________________\n")