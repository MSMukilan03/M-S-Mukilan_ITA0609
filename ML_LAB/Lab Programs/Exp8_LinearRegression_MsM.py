import pandas as pd
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Balls": [20,35,40,50,60,70,80,90],
    "Runs": [25,45,50,65,80,95,110,125]
}

df = pd.DataFrame(data)

X = df[["Balls"]]
y = df["Runs"]

model = LinearRegression()
model.fit(X, y)

# Predict using DataFrame
new_data = pd.DataFrame({"Balls": [55]})
prediction = model.predict(new_data)

print("Predicted Runs for 55 balls =", prediction[0])
print("Slope =", model.coef_[0])
print("Intercept =", model.intercept_)
