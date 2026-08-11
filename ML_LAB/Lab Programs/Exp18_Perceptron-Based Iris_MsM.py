from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = load_iris()

# Use only Setosa and Versicolor
X = iris.data[:100, [0, 2]]
y = iris.target[:100]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Perceptron
model = Perceptron(random_state=42)

# Train
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
print("Perceptron Accuracy:", accuracy_score(y_test, y_pred))

# New flower
new_flower = [[5.1, 1.4]]

prediction = model.predict(new_flower)

print("Predicted Flower:",
      iris.target_names[prediction[0]])
