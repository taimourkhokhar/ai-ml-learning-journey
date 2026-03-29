#4 Count how many times each element appears frequency

# nums=[1,2,2,3,4]
# new=[]
# for i in nums:
#   if i not in new:
#     new.append(i)
#     count=nums.count(i)
#     print(count)
# print(new)

# nums=[1,2,3,4,4]
# freq={}
# for i in nums:
#   if i in freq:
#     freq[i]+=1
#   else:
#     freq[i]=1
# print(freq)



#Rotate a list to the right by k steps

# nums=[1,2,3,4]
# step=2
# for i in range(step):
#  last=nums.pop()
#  nums.insert(0,last)
# print(nums)



#3 Dictionaires

#1 Create a dictioinary of students and find the highest marks

# students = {
#     "Taimour": 85,
#     "Alice": 92,
#     "Bob": 78,
#     "Charlie": 95,
#     "Diana": 88
# }


# highest=0
# name=""
# for key,val in students.items():
#   if val>highest:
#     highest=val
#     name=key
# print("Higest score is ",name,highest)


#2 Count a frequency of characters ina string using dictionary

# string="Hello again Hello "

# freq={}

# for i in string:
#   if i in freq:
#     freq[i]+=1
#   else:
#     freq[i]=1
# print(freq)

# chars=["a","a","b","b","c","c","c"]
# count=[]
# for i in chars:
#   if i not in count:
#     count.append(i)
#     count=chars.count(i)
#     print(count)
# print(count)



# nums=[1,2,2,3,4]
# new=[]
# for i in nums:
#   if i not in new:
#     new.append(i)
#     count=nums.count(i)
#     print(count)
# print(new)



chars = ["a", "a", "b", "b", "c", "c", "c"]
unique_chars = []
counts = []

for i in chars:
    if i not in unique_chars:
        unique_chars.append(i)
        count_value = chars.count(i)
        counts.append(count_value)
        print(f"Character {i} appears {count_value} times")

print("Final counts list:", counts)