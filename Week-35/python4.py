# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         i, j = 0, 0
        
#         while i < len(s) and j < len(t):
#             if s[i] == t[j]:
#                 i += 1
#             j += 1
            
#         return i == len(s)


# s = "Hello World"
# last_word=s.split()
# print(len(last_word[-1]))
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def introduce(self):
#         print("name of person",self.name,"age is ",self.age)

# class student(person):
#     def __init__(self, name, age,student_id):
#         super().__init__(name, age)
#         self.student_id=student_id
#     def display_student(self):
#         print("name of student",self.name,"age is ",self.age,"student id is ",self.student_id)

# pr=person("ati",22)
# pr.introduce()

# st=student("Taimour",22,2212)
# st.display_student()

# class Animal:
#       def make_sound(self):
#             print("Sound")
# class Cat(Animal):
#       def make_sound(self):
#             print("meow")
# class Dog(Animal):
#       def make_sound(self):
#             print("woo wo")
# ct=Cat()
# ct.make_sound()
# dg=Dog()
# dg.make_sound()

# def count_upto(n):
#     count=1
#     while count<=n:
#         yield count
#         count+=1
# for num in count_upto(10):
#     print(num)


# def even_number():
#     count=1
#     while count<=50:
#         if count%2==0:
#             yield count
        
#         count+=1
# for num in even_number():
#     print(num)

# def read_line():
#  with open("learning_log.txt","r") as f:
#     for i in f.read().splitlines():
#       if "error" in i:
#         yield i
# for value  in read_line():
#   print(value)

# numbers = [10, 20, 30, 40, 50]
# myit=iter(numbers)
# print(next(myit))

# class countdown:
#     def __init__(self,start):
#         self.current=start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.current<0:
#             raise StopIteration
#         value=self.current
#         self.current-=1
#         return value

# Countdown=countdown(5)
# for num in Countdown:
#     print(num)

# class MyNumbers:
#     def __iter__(self):
#         self.a=1
#         return self
#     def __next__(self):
#         if self.a<=20:
#             x=self.a
#             self.a+=1
#             return x
#         else:
#             raise StopIteration
# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)


# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# nums=[0,1,0,3,12]
# left=0
# right=len(nums)-1
# while left<right:
#     if nums[right]!=0:
#         nums[left],nums[right]=nums[right],nums[left]
#         left+=1
#         right-=1
#     else:
#         left+=1
#         right-=1
# print(nums)



nums = [0, 1, 0, 3, 12]
left = 0
right = len(nums) - 1

while left < right:
    if nums[left] != 0:
        # Left is already non-zero, leave it and check the next element
        left += 1
    elif nums[right] == 0:
        # Right is already zero, leave it and move inward
        right -= 1
    else:
        # nums[left] is 0 and nums[right] is non-zero -> Swap!
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

print(nums)  # Output: [12, 1, 3, 0, 0]