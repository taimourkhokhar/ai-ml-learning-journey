import pandas as pd
# print(pd.__version__)

#series in pandas is one dimensional array

# data=[100.1,102.1,104.1]
# series=pd.Series(data,index=["apartment1","apartment2","apartment3"])

# print(series)

# data1=[100,102,104,200,202]


# series1=pd.Series(data1,index=["a","b","c","d","e"])
# # series1.loc["c"]=200
# # print(series1.loc["a"])
# # print(series1.iloc[0])
# print(series1[series1>=200])


# calories={"Day 1":1750,"Day 2": 2200, "Day 3":1599}
# series=pd.Series(calories)
# print(series.loc["Day 1"])


# data={"Name":["Spongebob","Patrick","Squidward"],
#       "Age":[39,33,32]}

# dataframe=pd.DataFrame(data,index=["Employee1","Employee2","Employee3"])

# print(dataframe.loc["Employee1"])

# #add a mew column

# dataframe["new"]=[1,2,3]

# #add a new row 

# new_row=pd.DataFrame([{"Name":"Sandy","Age":22,"new":4}])
# dataframe=pd.concat([dataframe,new_row])
# print(dataframe.iloc[0])
# print(dataframe)


# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

import pandas as pd

#aggregate function in pandas
#  Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]

# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k=3
# left=0
# zero_count=0
# max_len=0
# for right in range(len(nums)):
#   if nums[right]==0:
#     zero_count+=1
#   while zero_count>2:
#     if nums[left]==0:
#       zero_count-=1
#     left+=1
#   max_len=max(max_len,right-left+1)

# print(max_len)