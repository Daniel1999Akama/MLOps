# SYNOPSIS
    # This is an example script used to demonstrate ML basic automation.
    # The train_model.sh shell script runs this file and outputs the findings.
    # The train_model.sh scripts runs line by line.
    # This is cool.



# importing needed libs

import pickle
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# loading data
data = load_iris()
x, y = data.data, data.target

# fitting model
model = LogisticRegression(max_iter=200)
model.fit(x, y)

# predicting
predictions = model.predict(x)
print("Accuracy: ", accuracy_score(y, predictions))

# saving the trained model
with open("iris_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved as iris_model.pkl")

