#This hash table will use chaining to handle collisions by allowing multiple key value pairs to be at the same bucket.
class HashTable: 
    def __init__(self, size = 40): #Initialize the hash table with a starting size of 40 for the total number of packages.
        self.table = [None] * size

    def getHash(self, key): #Hash function
        return hash(key) % len(self.table)
    
    #Insertion function that uses simple chaining if an element already exists at bucket.
    def insertItem(self, key, value):
        bucket = self.getHash(key)
        keyValue = [key, value]
    
        if self.table[bucket] == None:
            self.table[bucket] = list([keyValue]) 
            return True
        else:
            for item in self.table[bucket]:
                if item[0] == key:
                    item[1] = value
                    return True
        self.table[bucket].append(keyValue)
        return True
    
    #Look up function.
    def lookUp(self, key):
        bucket = self.getHash(key)
        if self.table[bucket] is not None:
            for item in self.table[bucket]:
                if item[0] == key:
                    return item[1]
            return None
            
    #Delete function.
    def deleteItem(self, key):
        bucket = self.getHash(key)
        element = 0
        for item in self.table[bucket]:
            if item[0] == key:
                self.table[bucket].pop(element)
                return True
            element += 1
        return False