import csv
import matplotlib.pyplot as plt

names = []
scores = []
colors = []

with open("churn_risk_report.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row["name"]
        score = float(row["churn_score"])

        names.append(name)
        scores.append(score)

        if score >= 10:
            colors.append("red")
        elif score >= 5:
            colors.append("orange")
        else:
            colors.append("green")


plt.figure(figsize=(10, 6))
plt.bar(names, scores, color=colors)
plt.title("Top Customers at Risk of Churning")
plt.xlabel("Customer")
plt.ylabel("Churn Score")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--")
plt.tight_layout()
plt.show()

