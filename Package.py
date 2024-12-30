class Package:

    def __init__(self, ID, address, city, state, zipCode, deliveryDeadline, weightKilos, specialNotes, status):
        
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deliveryDeadline = deliveryDeadline
        self.weightKilos = weightKilos
        self.specialNotes = specialNotes
        self.status = status

    def __str__(self):
        return (f"Package ID: {self.ID}\n" 
                f"Address: {self.address}, {self.city}, {self.state}, {self.zipCode}\n" 
                f"Weight: {self.weightKilos}kg \n" 
                f"Status: {self.status}\n"
                f"Delivery Deadline: {self.deliveryDeadline}\n" 
                f"Notes: {self.specialNotes}\n" 
                "_____________________________________________________________________________\n")