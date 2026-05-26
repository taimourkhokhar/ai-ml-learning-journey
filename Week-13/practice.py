nums1 = [1,2,3]
nums2 = [2,4,6]

s_num1=set(nums1)
s_num2=set(nums2)

diff_1=s_num1.difference(s_num2)
diff_2=s_num2.difference(s_num1)

print(list([diff_1,diff_2]))