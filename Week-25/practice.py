# nums = [1,1,0,1]
# for right in range(len(nums)-1):
#   if nums[right]==0:
#     nums.pop(right)

# print(len(nums))

#bar chart in matplotlib


import matplotlib.pyplot as plt
# categories=["Freshman","Sophomores","Juniors","Seniors"]
# values=[300,250,275,225]
# colors=["red","yellow","blue","green"]
# plt.pie(values,labels=categories,autopct="%1.1f",colors=colors,explode=[0,0,0,1])
# plt.show()

#scatter graph

# x=[0,1,1,2,3,4,5,6,7,7,8]
# y=[55,69,62,67,78,77,56,88,88,88,99]
# plt.scatter(x,y)
# plt.xlabel("Hours Studied")
# plt.ylabel("Grades")
# plt.show()

#histogram

import  numpy as np

# scores=np.random.normal(loc=80,scale=10,size=100)
# scores=np.clip(scores,0,100)
# plt.hist(scores,bins=10,color="lightgreen",edgecolor="black")
# plt.show()


# x=np.array([1,2,3,4,5])
# figure,axes=plt.subplots(2,2)
# axes[0,0].plot(x,x*2)
# plt.show()