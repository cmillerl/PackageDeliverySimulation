class HashTable: #This hash table will use chaining to handle collisions by allowing multiple key value pairs to be at the same index.
    def __init__(self, size = 40): #Initialize the hash table with a starting size of 40 for the total number of packages.
        self.table = [None] * size

    def getHash(self, key): #Hash function
        return hash(key) % len(self.table)
    
    def insertItem(self, key, value): #Insertion function that uses simple chaining if an element already exists at index.
        index = self.getHash(key)
        keyValue = [key, value]
    
        if self.table[index] == None:
            self.table[index] = list([keyValue]) 
            return True
        else:
            for item in self.table[index]:
                if item[0] == key:
                    item[1] = value
                    return True
        self.table[index].append(keyValue)
        return True
    
    def lookUp(self, key): #Look-up function.
        for item in self.table[self.getHash(key)] or []:
            if item[0] == key:
                return item[1]
            else:
                return None
            
    def deleteItem(self, key): #Delete function.
        index = self.getHash(key)
        element = 0
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].pop(element)
                return True
            element += 1
        return False