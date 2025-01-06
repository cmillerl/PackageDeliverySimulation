#This hash table will use chaining to handle collisions by allowing multiple key value pairs to be at the same bucket.
class HashTable: 
    #Initialize the hash table with a starting size of 40 for the total number of packages.
    def __init__(self, size = 40):
        self.table = [None] * size
        self.size = size
        self.itemsInside = 0

    #Hash function that will return the hash value of the key.
    #O(1)
    def getHash(self, key): #Hash function
        return hash(key) % len(self.table)
    
    #Insertion function that uses simple chaining if an element already exists at bucket.
    #If the table is full, it will resize the table.
    #O(1) unless the table needs to be resized.
    def insertItem(self, key, value):
        bucket = self.getHash(key)
        keyValue = [key, value]
    
        if self.table[bucket] == None:
            self.table[bucket] = list([keyValue]) 
            self.itemsInside += 1
            return True
        else:
            for item in self.table[bucket]:
                if item[0] == key:
                    item[1] = value
                    return True
        self.table[bucket].append(keyValue)
        self.itemsInside += 1

        if self.itemsInside >= self.size:
            self.resizeTable()
        return True
    
    #Look up function.
    #O(1)
    def lookUp(self, key):
        bucket = self.getHash(key)
        if self.table[bucket]:
            for item in self.table[bucket]:
                if item[0] == key:
                    return item[1]
            return None
            
    #Delete function.
    #O(1)
    def deleteItem(self, key):
        bucket = self.getHash(key)
        element = 0
        for item in self.table[bucket]:
            if item[0] == key:
                self.table[bucket].pop(element)
                return True
            element += 1
        return False
    
    #Resize function.
    #O(N)
    def resizeTable(self):
        oldTable = self.table
        self.size = self.size * 2
        self.table = [None] * self.size
        
        for bucket in oldTable:
            if bucket is not None:
                for key, value in bucket:
                    self.insertItem(key, value)

    #Get the size of the hash table, useful for debugging.
    #O(1)
    def getSize(self):
        return(self.size)