import os
import joblib
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load Dataset
df = pd.read_csv("Rainfall.csv")

print("\nFirst 5 Rows\n")
print(df.head())

print("\nDataset Info\n")
print(df.info())

# Remove extra spaces in column names

df.columns = df.columns.str.strip()

# Convert target variable
# yes -> 1
# no -> 0
df["rainfall"] = df["rainfall"].map({
    "yes":1,
    "no":0
})

# Features and Target
X = df.drop("rainfall", axis=1)
y = df["rainfall"]


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining Samples :", len(X_train))
print("Testing Samples :", len(X_test))

# Create Decision Tree
model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=5,
    min_samples_split=10,
    min_samples_leaf=5,
    random_state=42
) 
# Train Model
model.fit(X_train, y_train)
print("\nModel Training Completed!")

# Prediction 
y_pred = model.predict(X_test)
print(y_pred[:20])

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("\nAccuracy")
print(round(accuracy*100,2),"%")
print("\nClassification Report\n")
print(classification_report(y_test,y_pred))
print("\nConfusion Matrix\n")
print(confusion_matrix(y_test,y_pred))


#creating confusion matrix figure

import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

ConfusionMatrixDisplay.from_estimator(
    model,
    X_test,
    y_test,
    cmap="Blues"
)

plt.title("Confusion Matrix")

plt.savefig("confusion_matrix.png")
print("Confusion_matrix created")
plt.close()

#creating feature_importance figure
importance = model.feature_importances_

columns = X.columns

plt.figure(figsize=(8,5))

plt.bar(columns,importance)

plt.title("Feature Importance")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("feature_importance.png")
print("feature_importance created")
plt.close()

# decision tree visualization
from sklearn.tree import plot_tree

plt.figure(figsize=(20,10))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["No Rain","Rain"],
    filled=True
)

plt.savefig("decision_tree.png")
print("decision_tree_visualization created")
plt.close()


# Save Model
os.makedirs("model",exist_ok=True)
joblib.dump(model,"model/rainfall_model.pkl")
print("\nModel Saved Successfully!")

print("="*40)

print("Accuracy :",round(accuracy*100,2),"%")

print("="*40) 