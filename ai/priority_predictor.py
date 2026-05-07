from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4]])
y = np.array([1, 2, 3, 4])

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[5]])

print("Predicted Priority:", prediction)
