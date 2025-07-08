import sqlite3 

connection = sqlite3.connect("churn_customers.db")
cursor = connection.cursor()

customers = [
    ("John Smith", 6.5), 
    ("Ana Lopez", -2.3),
    ("Leo King", -7.1),
    ("Maria Torres", 11.0),
    ("Jane Lee", -9.7),
    ("Bob Allen", 1.4)
]

cursor.executemany("INSERT INTO customers (name, churn_score) VALUES (?, ?)", customers)

print(f"✅ Inserted {len(customers)} customer records.")

connection.commit()
connection.close()