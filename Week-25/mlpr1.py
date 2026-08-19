# import numpy as np

# x = np.array([1, 2, 3, 4, 5])
# y = np.array([2, 4, 6, 8, 10])

# n = len(x)

# x_mean = np.mean(x)
# y_mean = np.mean(y)

# print(x)

# b1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)

# b0 = y_mean - b1 * x_mean

# print("Slope:", b1)
# print("Intercept:", b0)

# # prediction
# x_new = 6

# prediction = b0 + b1 * x_new

# print("Prediction:", prediction)


# import numpy as np
# from sklearn.linear_model import LinearRegression

# x = np.array([[1], [2], [3], [4], [5]])
# y = np.array([2, 4, 6, 8, 10])

# model = LinearRegression()

# model.fit(x, y)

# print("Slope:", model.coef_)
# print("Intercept:", model.intercept_)

# prediction = model.predict([[6]])

# print("Prediction:", prediction)


# x=[1,2,3,4,5]
# y=[3,5,7,9,11]
# x_val=0
# for i in x:
#   x_val+=i
# x_mean=x_val/len(x)
# print(x_mean)

# y_val=0
# for i in y:
#   y_val+=i
# y_mean=y_val/len(y)
# print(y_mean)

# x_val1=[]
# y_val1=[]
# for i,j in zip(x,y):
#   x_val1.append(i-x_mean)
#   y_val1.append(j-y_mean)

# upper=0
# print(x_val1,y_val1)
# for i,j in zip(x_val1,y_val1):
#   upper+=i*j
# print(upper)

# lower=0
# for i in x_val1:
#    lower+=i**2

# print(lower)

# b1=upper/lower

# b0=y_mean-b1*x_mean

# print("slope is ",b1)
# print("intercept is ", b0)

# x=10

# y=b0+b1*x

# print("predicted value is ", y)

# def linear_regression(x,y):
#   x_mean=sum(x)/len(x)
#   y_mean=sum(y)/len(y)
#   x_val1=[i-x_mean for i in x]
#   y_val1=[j-y_mean for j in y]
#   upper=sum(i*j for i,j in zip(x_val1,y_val1))
#   lower=0
#   for i in x_val1:
#     lower+=i**2
#   b1=upper/lower
#   b0=y_mean-(b1*x_mean)
#   return b0,b1

# import numpy as np
# from sklearn.linear_model import LinearRegression
# X = np.array([[1], [2], [3], [4], [5]])
# y = np.array([3, 5, 7, 9, 11])


# lg=LinearRegression()
# lg.fit(X,y)

# print("b1",lg.coef_)
# print("b0",lg.intercept_)

# output=lg.predict([[10]])
# print(output)
# import numpy as np
# from sklearn.linear_model import LinearRegression
# x = np.array([
#     [1000, 2],
#     [1500, 3],
#     [2000, 4],
#     [2500, 4],
#     [3000, 5]
# ])
# y=np.array([10,15,20,25,30])
# lg=LinearRegression()
# lg.fit(x,y)
# print("b1",lg.coef_)
# print("b0",lg.intercept_)

# output=lg.predict([[1800,3]])
# print(output)