import sqlite3

connection = sqlite3.connect("churn_customers.db")
cursor = connection.cursor()

cursor.execute("""
SELECT customer_id, name, churn_score
FROM customers
WHERE churn_score > 5
ORDER  BY churn_score DESC
""")

high_risk_customers = cursor.fetchall()

print("🚨 Top Customers at Risk of Churning:")
for customer in high_risk_customers:
    print(f"ID: {customer[0]}, Name: {customer[1]}, Churn Score: {customer[2]}")

connection.close()