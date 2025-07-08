import sqlite3
import csv

connection = sqlite3.connect("churn_customers.db")
cursor = connection.cursor()

cursor.execute("""
SELECT customer_id, name, churn_score
FROM customers
WHERE churn_score > 5
ORDER BY churn_score DESC
""")

high_risk_customers = cursor.fetchall()

with open("churn_risk_report.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Customer Id", "Name", "Churn Score"])
    writer.writerows(high_risk_customers)

print("✅ High-risk churn report exported as 'churn_risk_report.csv'.")

connection.close()


