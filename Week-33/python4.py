# import random
# from math_utils import maximum

# questions=[{"q1":"What is your name?"},{"q2":"How old are you?"},{"q3":"where do you live?"}]
# print(random.choice(questions))

# ls=[1,2,3,4,5]
# print(maximum(ls))


import numpy as np

data=[10,20,30,40,50]
arr=np.array(data)

mean_value=np.mean(arr)
std_val=np.std(arr)

numpy_version=np.__version__

print(f"NumPy Version: {numpy_version}")
print(f"Array: {arr}")
print(f"Mean: {mean_value}")
print(f"Standard Deviation: {std_val}")
