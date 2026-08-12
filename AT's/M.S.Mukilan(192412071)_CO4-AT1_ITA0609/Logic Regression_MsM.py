import math

data = [
    [20, 85, 0],
    [25, 90, 0],
    [30, 95, 0],
    [35, 100, 0],
    [40, 105, 0],
    [45, 110, 0],
    [50, 115, 1],
    [55, 120, 1],
    [60, 125, 1],
    [65, 130, 1],
    [70, 135, 1],
    [75, 140, 1]
]

X = []
y = []

for row in data:
    X.append([row[0] / 100, row[1] / 150])
    y.append(row[2])

def sigmoid(z):
    if z < -500:
        return 0
    if z > 500:
        return 1
    return 1 / (1 + math.exp(-z))

def train_logistic_regression(X, y, learning_rate, epochs):
    w1 = 0.0
    w2 = 0.0
    bias = 0.0

    n = len(X)

    for epoch in range(epochs):
        dw1 = 0
        dw2 = 0
        db = 0

        for i in range(n):
            x1 = X[i][0]
            x2 = X[i][1]

            z = w1 * x1 + w2 * x2 + bias
            prediction = sigmoid(z)
            error = prediction - y[i]

            dw1 += error * x1
            dw2 += error * x2
            db += error

        dw1 /= n
        dw2 /= n
        db /= n

        w1 -= learning_rate * dw1
        w2 -= learning_rate * dw2
        bias -= learning_rate * db

    return w1, w2, bias

def predict(X, w1, w2, bias):
    results = []

    for row in X:
        z = w1 * row[0] + w2 * row[1] + bias
        probability = sigmoid(z)

        if probability >= 0.5:
            predicted_class = 1
        else:
            predicted_class = 0

        results.append((probability, predicted_class))

    return results

print("LOGISTIC REGRESSION - CRICKET PREDICTION")

learning_rate = float(input("Enter learning rate: "))
epochs = int(input("Enter number of epochs: "))

w1, w2, bias = train_logistic_regression(
    X, y, learning_rate, epochs
)

print("\nFinal Weight 1:", round(w1, 4))
print("Final Weight 2:", round(w2, 4))
print("Final Bias:", round(bias, 4))

results = predict(X, w1, w2, bias)

correct = 0

print("\nCLASSIFICATION RESULTS")

for i in range(len(X)):
    probability = results[i][0]
    predicted = results[i][1]
    actual = y[i]

    print(
        "Player", i + 1,
        "| Actual:", actual,
        "| Sigmoid:", round(probability, 4),
        "| Predicted:", predicted
    )

    if predicted == actual:
        correct += 1

accuracy = (correct / len(y)) * 100

print("\nCorrect Predictions:", correct)
print("Total Samples:", len(y))
print("Accuracy:", round(accuracy, 2), "%")

print("\nNEW PLAYER PREDICTION")

runs = float(input("Enter previous match runs: "))
strike_rate = float(input("Enter strike rate: "))

x1 = runs / 100
x2 = strike_rate / 150

z = w1 * x1 + w2 * x2 + bias
probability = sigmoid(z)

if probability >= 0.5:
    prediction = 1
    result = "Likely to score 50+ runs"
else:
    prediction = 0
    result = "Unlikely to score 50+ runs"

print("Sigmoid Output:", round(probability, 4))
print("Predicted Class:", prediction)
print("Result:", result)
