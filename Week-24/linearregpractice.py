import numpy as np
import matplotlib.pyplot as plt
hours=[1,2,3,4,5,6,7,8]
scores=[35,40,50,55,65,70,78,85]

hours=np.array(hours)
scores=np.array(scores)

hours=hours.reshape(1,-1)

print(hours.ndim)

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(hours,scores,test_size=0.2,random_state=42)
print(len(x_train))
print(len(y_test))