import numpy as np

def gradient_descent(x, y):
    m = b = 0
    iterations = 1000
    lr = 0.001
    n = len(x)

    for i in range(iterations):
        y_pred = m * x + b
        
        md = -(2/n) * np.sum(x * (y - y_pred))
        bd = -(2/n) * np.sum(y - y_pred)
        cost=(1/n)*sum([val**2 for val in (y-y_pred)])
        m = m - lr * md
        b = b - lr * bd

        if i % 100 == 0:
            print(f"Iteration {i}: m={m}, b={b}, cost={cost}")

    return m, b

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x, y)