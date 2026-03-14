# def get_hash(key):
#   h=0
#   for char in key:
#     h+=ord(char)#ord function find ascii value

#   return h%100



# print(get_hash('march 6'))




# print(ord('a'))


# class HashTable:
#   def __init__(self):
#     self.MAX=100
#     self.arr=[None for i in range(self.MAX)]

#   def get_hash(self,key):
#     h=0
#     for char in key:
#       h+=ord(char)
#     return h%self.MAX
  
#   def add(self,key,val):
#     h=self.get_hash(key)
#     self.arr[h]=val

#   def get(self,key):
#     h=self.get_hash(key)
#     return self.arr[h]


# t=HashTable()
# print(t.get_hash("march 6"))
# t.add('march 6',130)
# t.add('march 17',22)

# print(t.get('march 6'))


#how to handle collision in hash table

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self, key, val):
        h = self.get_hash(key)

        found = False
        for idx, element in enumerate(self.arr[h]):
            if element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break

        if not found:
            self.arr[h].append((key, val))

    def get(self, key):
        h = self.get_hash(key)

        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

        return None
    
    def __delitem__(self, key):
       h=self.get_hash(key)
       for index, element in enumerate(self.arr[h]):
           if element[0]==key:
               del self.arr[h][index]

t = HashTable()

t.add('march 6',130)
t.add('march 17',22)

print(t.get('march 6'))
print(t.get('march 17'))
del t["march 17"]
print(t.get('march 17'))
