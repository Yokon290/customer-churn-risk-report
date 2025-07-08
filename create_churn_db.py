import sqlite3

connection = sqlite3.connect("churn_customers.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    churn_score REAL NOT NULL
)
""")

print("✅ Database and table created sucessfully.")

connection.commit()
connection.close()
