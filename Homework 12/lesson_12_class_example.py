"""Lesson 12 — Logistic Regression və Classification Metrics.

Classroom example: customer churn prediction using a small synthetic dataset.
Run: python lesson_12_class_example.py
Dependencies: pandas, scikit-learn
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score,
)


# 1. Dataset: weekly logins, support tickets, and churn (1 = left, 0 = stayed).
df = pd.DataFrame({
    "weekly_logins": [
        1, 2, 1, 3, 4, 2, 3, 4,
        5, 5, 6, 2, 1, 8, 9, 10,
        7, 6, 11, 8, 12, 10, 9, 7,
        4, 6, 5, 3, 8, 2, 11, 4,
    ],
    "support_tickets": [
        4, 3, 5, 3, 2, 5, 2, 4,
        4, 1, 3, 1, 3, 0, 1, 0,
        2, 1, 0, 2, 0, 1, 2, 1,
        2, 4, 1, 3, 1, 2, 1, 0,
    ],
    "churn": [
        1, 1, 1, 1, 1, 1, 1, 1,
        1, 0, 0, 1, 1, 0, 0, 0,
        0, 0, 0, 0, 0, 0, 0, 0,
        1, 1, 0, 1, 0, 1, 0, 0,
    ],
})

print("First five rows:")
print(df.head())
print("\nChurn counts:")
print(df["churn"].value_counts())

# 2. Features and target.
X = df[["weekly_logins", "support_tickets"]]
y = df["churn"]

print("\nFeatures:")
print(X.head())
print("\nTarget:")
print(y.head())

# 3. Train/test split (same seed and stratification as in class).
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=22,
    stratify=y,
)

print("\nTrain size:", len(X_train))
print("Test size:", len(X_test))

# 4. Train Logistic Regression and predict labels.
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("\nReal values:")
print(y_test.to_list())
print("Predictions:")
print(y_pred)

# 5. Predict probabilities for both classes, then for churn (class 1).
print("\nClasses:")
print(model.classes_)
print("Probabilities:")
print(model.predict_proba(X_test))

churn_probabilities = model.predict_proba(X_test)[:, 1]
print("\nChurn probabilities:")
print(churn_probabilities)

results = X_test.copy()
results["actual"] = y_test
results["predicted"] = y_pred
results["churn_probability"] = churn_probabilities.round(3)

print("\nResults sorted by churn probability:")
print(results.sort_values("churn_probability"))

# 6. Default threshold = 0.5; then reduce it to 0.3.
threshold = 0.5
custom_predictions = (churn_probabilities >= threshold).astype(int)
print("\nCustom predictions at 0.5:")
print(custom_predictions)
print("Default model predictions:")
print(y_pred)

threshold = 0.3
predictions_03 = (churn_probabilities >= threshold).astype(int)
results["predicted_03"] = predictions_03

print("\nThreshold 0.3 compared with default predictions:")
print(
    results[
        ["actual", "churn_probability", "predicted", "predicted_03"]
    ].sort_values("churn_probability")
)

# 7. Confusion matrix: [[TN, FP], [FN, TP]].
cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
print("\nConfusion Matrix:")
print(cm)

tn = cm[0, 0]
fp = cm[0, 1]
fn = cm[1, 0]
tp = cm[1, 1]
print("True Negative:", tn)
print("False Positive:", fp)
print("False Negative:", fn)
print("True Positive:", tp)

errors = results[results["actual"] != results["predicted"]]
print("\nWrong predictions:")
print(errors)

# 8. Classification metrics.
print("\nModel Evaluation")
print("Accuracy:", round(accuracy_score(y_test, y_pred), 2))
print("Precision:", round(precision_score(y_test, y_pred), 2))
print("Recall:", round(recall_score(y_test, y_pred), 2))
print("F1 Score:", round(f1_score(y_test, y_pred), 2))

# 9. Compare three thresholds with the SAME trained model.
for threshold in [0.3, 0.5, 0.7]:
    predictions = (churn_probabilities >= threshold).astype(int)
    print("\nThreshold:", threshold)
    print("Accuracy:", round(accuracy_score(y_test, predictions), 2))
    print("Precision:", round(precision_score(y_test, predictions), 2))
    print("Recall:", round(recall_score(y_test, predictions), 2))
    print("F1 Score:", round(f1_score(y_test, predictions), 2))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, predictions, labels=[0, 1]))

# 10. Extra threshold comparison from the final student exercise.
for threshold in [0.35, 0.5, 0.65]:
    predictions = (churn_probabilities >= threshold).astype(int)
    print("\nThreshold:", threshold)
    print("Precision:", round(precision_score(y_test, predictions), 2))
    print("Recall:", round(recall_score(y_test, predictions), 2))
