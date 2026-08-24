import numpy as np
# X = np.array([1, 2, 3, 4, 5])
# y = np.array([3, 5, 7, 9, 11])
# # for predication
# def predict(X):
#     return 2 * X + 1

# predicted = predict(X)
# print("Predictions:", predicted)


# def compute_cost(predicted, y):
#     return np.mean((predicted - y) ** 2)

# cost = compute_cost(predicted, y)
# print("Cost (MSE):", cost)



# w=0.0
# b=0.0
# learning_rate=0.01
# N=len(X)

# prediction=w*X+b

# #gradient

# dj_dw=(2/N)*np.sum((prediction-y)*X)
# dj_db=(2/N)*np.sum(prediction-y)

# w=w-learning_rate*dj_dw
# b=b-learning_rate*dj_db

# print(f"Gradient w: {dj_dw}, Gradient b: {dj_db}")
# print(f"Updated w: {w}, Updated b: {b}")



# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
# X = np.array([[1], [2], [3],[ 4], [5]])
# y = np.array([3, 5, 7, 9, 11])
# lg=LinearRegression()
# lg.fit(X,y)

# print(lg.coef_)
# print(lg.intercept_)

# actual=[5,9,13]
# test=[[2],[4],[6]]

# predicted=lg.predict(test)
# print(predicted)

# mse=mean_squared_error(actual,predicted)
# print(mse)

import numpy as np

X = np.array([1, 2, 3, 4, 5])
y = np.array([3, 5, 7, 9, 11])

w = 0
b = 0

learning_rate = 0.01
iterations = 1000


def predict(X, w, b):
    return w * X + b


def compute_cost(predicted, y):
    return np.mean((predicted - y) ** 2)


def compute_gradient(X, y, w, b):

    prediction = predict(X, w, b)

    dj_dw = (2 / len(X)) * np.sum((prediction - y) * X)
    dj_db = (2 / len(X)) * np.sum(prediction - y)

    return dj_dw, dj_db


def gradient_descent(X, y, w, b, learning_rate, iterations):

    for i in range(iterations):

        dj_dw, dj_db = compute_gradient(X, y, w, b)

        w = w - learning_rate * dj_dw
        b = b - learning_rate * dj_db

        if (i + 1) % 100 == 0 or i == 0:
            cost = compute_cost(predict(X, w, b), y)

            print(
                f"Iteration {i+1:4d} | "
                f"Cost: {cost:.6f} | "
                f"w: {w:.4f} | "
                f"b: {b:.4f}"
            )

    return w, b


w_final, b_final = gradient_descent(
    X, y, w, b, learning_rate, iterations
)

print("\nFinal Model Parameters:")
print(f"w: {w_final:.4f}")
print(f"b: {b_final:.4f}")