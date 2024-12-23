class Package:
    def __init__(self, ID, address, city, state, zipCode, deliveryDeadline, weightKilos, specialNotes):
        
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zipCode
        self.deliveryDeadline = deliveryDeadline
        self.weightKilos = weightKilos
        self.specialNotes = specialNotes