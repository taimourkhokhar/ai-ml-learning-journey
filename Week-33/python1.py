# name="Taimour"
# semester=7
# cgpa=3.15
# learing_AI=True
# print(f"My name is {name} right now i am in {semester} semester and my cgpa is {cgpa} and currently i am learning aiml {learing_AI}")

# obtained_marks=int(input("Enter obtained marks:"))
# total_marks=int(input("Enter total marks:"))
# percentage=obtained_marks/total_marks*100
# result=round(percentage,2)
# print(result)

# sentence=" My name is Taimour. I live in Lahore"
# print(sentence.replace(" ",""))
# print(sentence.split())
# count=0
# for i in sentence.split():
#     count+=1
# print(count)
# print(f"first word is {sentence[0]} and second word is {sentence[-1]}")

# marks=[30,50,80,90,70]
# average=0
# for i in marks:
#     average+=i
# print(average/len(marks))
# print(max(marks),min(marks))
# count=0
# for i in marks:
#     if i>=50:
#         count+=1
# print(count)

# sentences="My name name is is Taimour!"
# sentence=sentences.lower().replace("!","")
# dic={}
# for i in sentence.split():
#     dic[i]=sentence.count(i)
# print(dic)

# duplicates=[1,2,2,3,4,4,4,5,1,6]
# unique_numbers=set(duplicates)
# print(unique_numbers)
# lahore_cordinates=(31.4704,74.2982)
# print(lahore_cordinates)

# score=int(input("Enter a score "))
# if score==80 and score<=100:
#     print("A grade")
# elif score>=60 and score<=80:
#     print("B grade")
# else:
#     print("We just count 2 grades")

# num = int(input("Enter a number: "))


# def prime(num):
#     if num <= 1:
#         print("Not a prime number")
#         return

#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             return
#     else:
#         print("Prime number")


# prime(num)

# ls=[1,2,3,-1,0]
# postive=0
# negative=0
# zero_value=0
# sum=0
# for i in ls:
#     if i>0:
#         postive+=1
#     elif i<0:
#         negative+=1
#     else:
#         zero_value+=1
#     sum+=i
# print(sum,postive,negative,zero_value)