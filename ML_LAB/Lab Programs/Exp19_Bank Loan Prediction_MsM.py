import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Bank loan dataset
data = {
    "Age": [22, 25, 28, 30, 32, 35, 38, 40, 42, 45,
            24, 29, 34, 39, 44],

    "Income": [20, 25, 30, 35, 40, 45, 50, 55, 60, 70,
               22, 32, 42, 52, 65],

    "Loan_Amount": [15, 18, 20, 22, 25, 25, 30, 30, 28, 25,
                    17, 20, 24, 27, 25],

    "Credit_Score": [580, 590, 600, 620, 640, 660, 680, 700,
                     720, 750, 570, 610, 650, 690, 730],

    "Existing_Loans": [3, 3, 2, 2, 2, 1, 1, 1, 0, 0,
                       3, 2, 2, 1, 0],

    "Loan_Status": [
        "No", "No", "No", "No", "No",
        "Yes", "Yes", "Yes", "Yes", "Yes",
        "No", "No", "Yes", "Yes", "Yes"
    ]
}

df = pd.DataFrame(data)

# Input features
X = df[[
    "Age",
    "Income",
    "Loan_Amount",
    "Credit_Score",
    "Existing_Loans"
]]

# Target
y = df["Loan_Status"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Naive Bayes
model = GaussianNB()

# Train
model.fit(X_train, y_train)

# Test
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))

# New customer
new_customer = pd.DataFrame(
    [[35, 50, 25, 680, 1]],
    columns=[
        "Age",
        "Income",
        "Loan_Amount",
        "Credit_Score",
        "Existing_Loans"
    ]
)

prediction = model.predict(new_customer)

print("Loan Prediction:", prediction[0])
