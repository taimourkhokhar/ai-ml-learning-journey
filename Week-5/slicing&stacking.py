#slicing
import numpy as np
# a=np.array([6,7,8,9])
# print(a[0:])


#slicing in 2-D array

# b=np.array([
#   [1,2,3,],
#   [4,5,6],
#   [7,8,9]
# ])


# print(b[1,2:3])#it will print [6]
# print(b[2,0])
# print(b[-1,0:2])
# print(b[0:,1:3])



#customer id and cutomer name

c=np.array([
  [101,'Mira'],
  [102,'Abdul'],
  [103,'Andrea']
])
#customer id purchase amount, purchase date
d=np.array([
  [101,250.50,'2023-08-01'],
  [102,150.00,'2023-08-02'],
  [103,300.75,'2023-08-01']

])

# new=np.hstack((c,d))//for horizental stacking

# print(new)


#few new customer

# e=np.array([
# [104,'Venkat'],
#    [105,'John'],
#    [106,'Kathy']
# ])

# new=np.vstack((c,e))#for vertical stacking
# print(new)



#for a reverse

# transactions=np.array([
#   [101,'Mohan',250.50,'2022-08-05'],
#   [102,'Bob',150.00,'2023-08-02'],
#   [103,'Fatima',300.75,'2023-08-01'],
#   [104,'David',400.20,'2023-08-03'],
#   [105,'Aryan',400.20,'2023-08-04']
# ])

# new=np.hsplit(transactions,[2])#horizent split
# print(new)


# new=np.vsplit(transactions,[2])#vertical split
# print(new)



# monthly_sales=np.array([30,33,35,28,42])

# ans=monthly_sales<32

# print(ans)


# exact_rev=monthly_sales[ans]

# print(exact_rev)


# newly=monthly_sales.argmax()

# print(newly)


# transactions=np.array([
#   [101,'Mohan',250.50,'2022-08-05'],
#   [102,'Bob',150.00,'2023-08-02'],
#   [103,'Fatima',300.75,'2023-08-01'],
#   [104,'David',400.20,'2023-08-03'],
#   [105,'Aryan',400.20,'2023-08-04']
# ])

# new=transactions[:,2].astype('float')

# print(new)

# ans=[transactions[:,0]=='102']
# print(ans)
