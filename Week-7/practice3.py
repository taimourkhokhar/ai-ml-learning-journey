# height = [1,8,6,2,5,4,8,3,7]
# def main(ls):
#  max_value=0
#  left=0
#  right=len(height)-1# 9-1 which is 8

#  while left<right:
#   width=right-left # here 9-0 so 8 is width

#   current_height=min(height[left],height[right])

#   current_area=width*current_height
#   max_value=max(max_value,current_area)
#   if height[left]<height[right]:
#     left+=1
#   else:
#     right-=1
#  return max_value

# print(main(height))