import pandas as pd
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("data.csv")

X = data[["amount", "days_overdue", "past_recovery", "risk"]]
y = data["recovered"]

model = LogisticRegression()
model.fit(X, y)

def predict_case(case):
    prob = model.predict_proba([case])[0][1]
    if prob > 0.7:
        priority = "HIGH"
    elif prob > 0.4:
        priority = "MEDIUM"
    else:
        priority = "LOW"
    return prob, priority
