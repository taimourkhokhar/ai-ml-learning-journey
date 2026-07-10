#generator that yields numbers 1 to 10
# def count_up_to(n):
#   count=1
#   while count<=n:
#     yield count
#     count+=1

# cn=count_up_to(10)#we can here do by loop
# print(next(cn))
# print(next(cn))
# print(next(cn))
# print(next(cn))

#create a generator that yields only even number from 1 to 50
# def even_number(n):
#   for i in range(1,n):
#     if i%2==0:
#      yield i
  

# ev=even_number(50)

# print(next(ev))
# print(next(ev))
# print(next(ev))


#create a generator that takes a list of names

# def names(ls):
#   for nm in ls:
#    yield nm

# ls=["Ali","Sara","Ahmad","Ayesha"]
# nm=names(ls)

# print(next(nm))
# print(next(nm))
# print(next(nm))


#iterator question start here

# numbers=[10,20,30,40,50]
# new=iter(numbers)

# print(next(new))
# print(next(new))
# print(next(new))


#create your own iterator class called countdown


# class countdown:
#   def __iter__(self):
#     self.count=5
#     return self
#   def __next__(self):
#     x=self.count
#     self.count-=1
#     return x
  
# cn=countdown()
# myiter=iter(cn)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

class Square:
    def __init__(self, n):
        self.n = n          
        self.current = 1    

    def __iter__(self):
        return self        

    def __next__(self):
        if self.current < self.n:
            result = self.current * self.current
            self.current += 1  
            return result
        else:
            raise StopIteration  

sq = Square(5)
myiter = iter(sq)

print(next(myiter))  
print(next(myiter))  
print(next(myiter))  
