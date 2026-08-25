# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# data = {
#     "Age": [22, 25, 30, 35, 40, 28, 32, 45, 27, 38],
#     "City": [
#         "Lahore", "Karachi", "Lahore", "Islamabad", "Karachi",
#         "Lahore", "Islamabad", "Karachi", "Lahore", "Islamabad"
#     ],
#     "Purchased": [0, 1, 1, 0, 1, 1, 0, 1, 0, 0]
# }

# df = pd.DataFrame(data)
# df_encoded = pd.get_dummies(df, columns=["City"], dtype=int)

# X = df_encoded.drop("Purchased", axis=1)
# y = df_encoded["Purchased"]


# x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)





# rg=LogisticRegression()
# rg.fit(x_train,y_train)

# predicted=rg.predict(x_test)

# print(predicted)
# accuracy=accuracy_score(y_test,predicted)
# print(accuracy)




# import pandas as pd
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.compose import ColumnTransformer
# from sklearn.preprocessing import OneHotEncoder
# from sklearn.pipeline import Pipeline

# data = {
#     "Age": [22, 25, 30, 35, 40, 28, 32, 45, 27, 38],
#     "City": [
#         "Lahore", "Karachi", "Lahore", "Islamabad", "Karachi",
#         "Lahore", "Islamabad", "Karachi", "Lahore", "Islamabad"
#     ],
#     "Purchased": [0, 1, 1, 0, 1, 1, 0, 1, 0, 0]
# }

# df = pd.DataFrame(data)
# X = df.drop("Purchased", axis=1)
# y = df["Purchased"]

# x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # 1. Define preprocessor
# ct = ColumnTransformer(
#     transformers=[("city_enc", OneHotEncoder(sparse_output=False, handle_unknown="ignore"), ["City"])],
#     remainder="passthrough"
# )

# # 2. Define pipeline combining preprocessor and model
# pipeline = Pipeline([
#     ("preprocessor", ct),
#     ("classifier", LogisticRegression())
# ])

# # 3. Fit pipeline directly on RAW training data
# pipeline.fit(x_train, y_train)

# # 4. Predict directly on RAW test data
# predicted = pipeline.predict(x_test)
# accuracy = accuracy_score(y_test, predicted)

# print("Predictions:", predicted)
# print("Accuracy:", accuracy)



import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data = {
    "Age": [22, 25, 30, 35, 40, 28, 32, 45, 27, 38, 31, 24],
    "City": [
        "Lahore", "Karachi", "Lahore", "Islamabad",
        "Karachi", "Lahore", "Islamabad", "Karachi",
        "Lahore", "Islamabad", "Karachi", "Lahore"
    ],
    "Result": [
        0, 1, 2, 0, 1, 2,
        0, 1, 2, 0, 1, 2
    ]
}
df = pd.DataFrame(data)
df_encoded = pd.get_dummies(df, columns=["City"], dtype=int)

X = df_encoded.drop("Result", axis=1)
y = df_encoded["Result"]


x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)





rg=LogisticRegression()
rg.fit(x_train,y_train)

predicted=rg.predict(x_test)

print(predicted)
accuracy=accuracy_score(y_test,predicted)
print(accuracy)

probabilities = rg.predict_proba(x_test)

print(probabilities)