nums =[-100000,-100000]
new=[]
for i in nums:
    if i<0:
        nm=-1*i
        new.append(nm)
    else:
        new.append(i)

print(new)

minimum=min(new)
print("Minimum value in the new list is:", minimum)