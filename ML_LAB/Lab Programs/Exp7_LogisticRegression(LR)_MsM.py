import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
data = {
    'Balls_Faced': [25, 35, 48, 60, 20, 55, 30, 70, 45, 18],
    'Strike_Rate': [120, 128, 135, 142, 110, 138, 125, 145, 130, 100],
    'Fours': [3, 4, 6, 8, 2, 7, 3, 10, 5, 1],
    'Fifty_Plus': [0, 0, 1, 1, 0, 1, 0, 1, 1, 0]
}

df = pd.DataFrame(data)
X = df[['Balls_Faced', 'Strike_Rate', 'Fours']]
y = df['Fifty_Plus']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Actual Values    :", list(y_test))
print("Predicted Values :", list(y_pred))
print("Accuracy =", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
new_match = pd.DataFrame({
    'Balls_Faced': [52],
    'Strike_Rate': [140],
    'Fours': [7]
})
prediction = model.predict(new_match)
if prediction[0] == 1:
    print("Prediction: Virat is likely to score 50+ runs")
else:
    print("Prediction: Virat is unlikely to score 50+ runs")
