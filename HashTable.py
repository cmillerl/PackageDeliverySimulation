class HashTable:
    def __init__(self, size = 40): # initialize the hash table with a starting size of 40 for the total number of packages.
        self.table = [None] * size

    def getHashKey(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self.getHashKey(key)
        keyValue = [key, value]
    
        if self.table[index] == None:
            self.table[index] = list([keyValue]) 
            return True
        else:
            for item in self.table[index]:
                if item[0] == key:
                    item[1] = value
                    return true
        self.table[index].append(keyValue)
        return True
    
    def retrieve(self, key):
        for item in self.table[self.getHashKey(key)]:
            if item[0] == key:
                return item[1]
            else:
                return None
            
    def delete(self, key):
        index = self.getHashKey(key)
        element = 0
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].pop(element)
                return True
            element += 1
        return False